import requests
import json
from datetime import datetime
import logging

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models, transaction
from django.utils import timezone
from django.db.models import ObjectDoesNotExist

from super5 import settings
from athletes.models import Athlete
from trainings.models import WorkoutDiary, TrainingSet, Exercise, Training


logger = logging.getLogger(__name__)


@transaction.atomic
def update_trainings_for_user(user):
    transaction_point = transaction.savepoint()
    response = None
    try:
        today = datetime.now().date()
        if user.athlete.week_day and (str(today.weekday()) in user.athlete.week_day):
            duration = Athlete.DURATION[user.athlete.training_duration][1].split(' ')[0]
            day = Training.objects.filter(
                workout_diary__user=user,
                date__lt=today
            ).count()
            training_diary = WorkoutDiary.objects.get(user=user)
            training = Training(workout_diary=training_diary)
            training.save()

            url = settings.TRAINING_SERVICE_URL
            headers = {'content-type': 'application/json'}

            payload = {
                "method": "get_exercise",
                "params": {
                    "access_key": settings.TRAINING_SERVICE_SECRET_KEY,
                    "duration": duration,
                    "level": user.athlete.level,
                    "train_days_amount_per_week": len(eval(user.athlete.week_day)),
                    "day": day

                },
                "jsonrpc": "2.0",
                "id": training.id,
            }
            response = requests.post(url, data=json.dumps(payload), headers=headers)

            response = response.json()
            result = response.get('result', None)
            tasks = result.get('tasks', None)
            set_number = 0
            for outer_set in tasks:
                inter_set = TrainingSet(
                    number_in_training=set_number,
                    training=training
                )
                set_number += 1
                inter_set.save()
                for outer_exercise in outer_set:
                    if not Exercise.objects.filter(
                        zone__slug=outer_exercise['muscle'],
                        target__slug=outer_exercise['train_type']
                    ).exists():
                        transaction.savepoint_rollback(transaction_point)

                    inner_exercise = Exercise.objects.get(
                        zone__slug=outer_exercise['muscle'],
                        target__slug=outer_exercise['train_type']
                    )
                    inter_set.exercises.add(inner_exercise.id)
    except Exception as e:
        transaction.savepoint_rollback(transaction_point)
        logger.critical(
            'Can not get data from train-resolver service. Exception: ' + str(e) + ' Response:' + str(response)
        )


class FiveUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        FiveUserManager.check_related_models_for_queryset(FiveUser.objects)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    @staticmethod
    def check_related_models_for_queryset(queryset):
        for user in queryset.all():
            try:
                user.athlete
            except ObjectDoesNotExist:
                athlete = Athlete()
                athlete.user = user
                athlete.save()
            try:
                user.workoutdiary
            except ObjectDoesNotExist:
                workout_diary = WorkoutDiary()
                workout_diary.user = user
                workout_diary.save()

    @staticmethod
    def check_trainings(queryset):
        for user in queryset.all():
            if len(user.workoutdiary.training_set.filter(date=timezone.now()).all()) < 1:
                update_trainings_for_user(user)

    def get_queryset(self):
        queryset = super(FiveUserManager, self).get_queryset()
        FiveUserManager.check_related_models_for_queryset(queryset)
        FiveUserManager.check_trainings(queryset)
        return queryset


class FiveUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = FiveUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
