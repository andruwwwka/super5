from django.db import models
from django.dispatch import receiver
from datetime import datetime
from super5 import settings


class Athlete(models.Model):

    MALE, FEMALE = 0, 1
    GENDER = (
        (MALE, 'мужской'),
        (FEMALE, 'женский')
    )

    LOW, LOW_MIDDLE, MIDDLE, HEIGHT, VERY_HIGH = 0, 1, 2, 3, 4
    LEVEL = (
        (LOW, 'низкий'),
        (LOW_MIDDLE, 'ниже среднего'),
        (MIDDLE, 'средний'),
        (HEIGHT, 'высокий'),
        (VERY_HIGH, 'очень высокий')
    )

    MIN5, MIN15, MIN30, MIN60 = 0, 1, 2, 3
    DURATION = (
        (MIN5, '5 минут'),
        (MIN15, '15 минут'),
        (MIN30, '30 минут'),
        (MIN60, '60 минут')
    )

    MON, TUE, WED, THU, FRI, SAT, SUN = 0, 1, 2, 3, 4, 5, 6
    WEEK_DAYS = (
        (MON, 'Понедельник'),
        (TUE, 'Вторник'),
        (WED, 'Среда'),
        (THU, 'Четверг'),
        (FRI, 'Пятница'),
        (SAT, 'Суббота'),
        (SUN, 'Воскресенье')
    )

    height = models.IntegerField(
        'Рост',
        null=True,
        blank=True
    )
    width = models.IntegerField(
        'Вес',
        null=True,
        blank=True
    )
    gender = models.IntegerField(
        'Пол',
        choices=GENDER,
        null=True,
        blank=True
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    level = models.IntegerField(
        'Уровень подготовки',
        choices=LEVEL,
        null=True,
        blank=True
    )
    training_duration = models.IntegerField(
        'Продолжительность тренировок',
        choices=DURATION,
        null=True,
        blank=True
    )
    birthday = models.DateField(
        'Дата рождения',
        null=True,
        blank=True
    )

    confirmed = models.BooleanField(
        'Подтвержден',
        blank=True,
        default=False
    )
    week_day = models.CharField(
        'День недели',
        max_length=25,
        null=True,
    )
    actual_date = models.DateTimeField(
        'Дата изменения данных',
        null=True,
        blank=True
    )

    def get_targets(self):
        for target in Target.objects.all():
            TargetPriority.objects.get_or_create(
                athlete=self,
                target_priority=target,
                defaults={
                    'athlete': self,
                    'priority': 0,
                    'target_priority': target
                }
            )
        return TargetPriority.objects.filter(athlete=self).order_by("priority")

    def get_zones(self):
        for zone in Zone.objects.all():
            ZonePriority.objects.get_or_create(
                athlete=self,
                zone_priority=zone,
                defaults={
                    'athlete': self,
                    'priority': 0,
                    'zone_priority': zone
                }
            )
        return ZonePriority.objects.filter(athlete=self).order_by("priority")

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.user.get_full_name()

    def exercise_length_in_seconds(self):
        return 60

    def chill_length_in_seconds(self):
        return 10

    @property
    def birthday_value(self):
        return self.birthday.strftime('%Y-%m-%d') if self.birthday else u'Дата рождения'


@receiver(models.signals.pre_save, sender=Athlete)
def set_actual_date(sender, **kwargs):
    instance = kwargs.get('instance')
    instance.actual_date = datetime.now()


class TargetPriority(models.Model):
    athlete = models.ForeignKey(Athlete, null=True, blank=False)
    priority = models.IntegerField(
        'Приоритет цели',
        null=True
    )
    target_priority = models.ForeignKey('Target', null=True, blank=False)

    @staticmethod
    def change(athlete, priority, **target_filter):
        target = Target.objects.get(**target_filter)
        prior, created = TargetPriority.objects.get_or_create(
            athlete=athlete,
            target_priority=target,
            defaults={
                'athlete': athlete,
                'target_priority': target
            }
        )
        prior.priority = priority
        prior.save()
        return prior

    class Meta:
        unique_together = ('athlete', 'priority', 'target_priority')
        verbose_name = "Приоритет цели"
        verbose_name_plural = "Приоритет целей"

    def __str__(self):
        return "%s - %s - %s" % (
            self.athlete, self.priority, self.target_priority)


class Target(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=127,
        null=True,
        unique=True
    )

    slug = models.SlugField(
        'Идентификатор типа тренировок',
        null=True,
        unique=True
    )

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"

    def __str__(self):
        return self.name


class ZonePriority(models.Model):
    athlete = models.ForeignKey(Athlete, null=True, blank=False)
    priority = models.IntegerField(
        'Приоритет',
        null=True
    )
    zone_priority = models.ForeignKey('Zone', null=True, blank=False)

    @staticmethod
    def change(athlete, priority, **target_filter):
        zone = Zone.objects.get(**target_filter)
        prior, created = ZonePriority.objects.get_or_create(
            athlete=athlete,
            zone_priority=zone,
            defaults={
                'athlete': athlete,
                'zone_priority': zone
            }
        )
        prior.priority = priority
        prior.save()
        return prior

    class Meta:
        unique_together = ('athlete', 'priority', 'zone_priority')
        verbose_name = "Приоритет зоны"
        verbose_name_plural = "Приоритет зон"

    def __str__(self):
        return "%s - %s - %s" % (
            self.athlete, self.priority, self.zone_priority)


class Zone(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=127,
        null=True,
        unique=True
    )

    slug = models.SlugField(
        'Идентификатор группы мышц',
        null=True,
        unique=True
    )

    class Meta:
        verbose_name = "Целевая зона"
        verbose_name_plural = "Целевые зоны"

    def __str__(self):
        return self.name
