import pymorphy2

import json
from utils.funcs import chunks, add_months, sub_months, month_text

from calendar import Calendar, MONDAY
from datetime import datetime, date, timedelta
from django.views import generic
from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from athletes.models import Athlete
from .serializations import TrainingSerializer
from .models import WorkoutDiary, Training

from athletes.serializations import AthleteAllDataSerializer


def get_training(user, current_date):
    try:
        return Training.objects.get(
            workout_diary__user=user,
            date=current_date
        )
    except Training.DoesNotExist:
        return None


class DiaryTrainingsView(generic.DetailView):
    model = WorkoutDiary
    template_name = 'trainings/diary.html'

    def get_object(self, queryset=None):
        return self.model.objects.get_or_create(user=self.request.user)[0]

    def get_context_data(self, **kwargs):

        def get_weekday_text(athlete, weekday):
            morph = pymorphy2.MorphAnalyzer()
            if athlete.week_day:
                for week_day in eval(athlete.week_day):
                    if weekday < int(week_day):
                        day_text = morph.parse(Athlete.WEEK_DAYS[int(week_day)][1])[0].inflect({'accs'}).word
                        return 'во' if Athlete.WEEK_DAYS[int(week_day)][0] == 1 else 'в', day_text
                day_text = morph.parse(Athlete.WEEK_DAYS[int(eval(athlete.week_day)[0])][1])[0].inflect({'accs'}).word
                return 'во' if Athlete.WEEK_DAYS[int(eval(athlete.week_day)[0])][0] == 1 else 'в', day_text
            return 'не', 'запланирована'

        athlete = Athlete.objects.get_or_create(user=self.request.user)[0]
        today = datetime.now().date()
        cal = Calendar(MONDAY)
        year = int(self.kwargs.get('year'))
        month = int(self.kwargs.get('month'))
        day = int(self.kwargs.get('day'))
        current_date = date(year, month, day)
        next_month = add_months(current_date, 1)
        prev_month = sub_months(current_date, 1)
        month_dates = list(cal.itermonthdates(year, month))
        trainings = Training.objects.filter(
            date__in=month_dates,
            workout_diary=self.object
        )
        month_dates_with_training = [
            (item, True) if athlete.week_day and item >= today
            and str(item.weekday()) in athlete.week_day
            else (item, trainings.filter(date=item).last())
            for item in month_dates
        ]
        splited = chunks(month_dates_with_training, 7)
        month = [(week[0][0].isocalendar()[1] == today.isocalendar()[1], week) for week in splited]
        training_today = athlete.week_day and (str(today.weekday()) in athlete.week_day)
        training = get_training(self.request.user, current_date)
        ctx = {
            'training': training,
            'today': today,
            'month': month,
            'prev_month': prev_month,
            'next_month': next_month,
            'current_month': month_text(current_date.month),
            'current_date': current_date,
            'current_weekday': Athlete.WEEK_DAYS[current_date.weekday()][1],
            'training_duration': athlete.get_training_duration_display(),
            'history': current_date < today,
            'training_today': training_today,
            'button_text': (True, 'Начать тренировку')
            if training_today else
            (False, 'Следующая тренировка %s %s' % get_weekday_text(athlete=athlete, weekday=today.weekday()))
        }
        return ctx


def get_training_queryset(user):
    return Training.objects.filter(
        workout_diary__user=user,
    )


class TrainingView(TemplateView):

    template_name = 'trainings/training.html'

    def get(self, request, *args, **kwargs):
        current_date = datetime.now().date()
        queryset = get_training_queryset(request.user).filter(current_date)
        serializer = TrainingSerializer(queryset, many=True)
        ctx = {
            'training': json.dumps(serializer.data),
            'current_date': current_date,
            'weekday': Athlete.WEEK_DAYS[current_date.weekday()][1],
        }
        return self.render_to_response(ctx)


class TrainingsViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, format=None):
        current_date = datetime.now().date()
        from_date = self.request.query_params.get('from_date', datetime.now().date())
        to_date = self.request.query_params.get('to_date', datetime.now().date() + timedelta(days=7))
        get_training(self.request.user, current_date)
        return Response({
            'trainings': TrainingSerializer(
                get_training_queryset(self.request.user).filter(
                    date__gte=from_date, date__lte=to_date
                ),
                many=True,
                context={'request': self.request}
            ).data,
            'user_athlete': AthleteAllDataSerializer().to_representation(self.request.user.athlete)
        })


def training_diary_current_month(request):
    now = datetime.now()
    return redirect('trainings:diary', year=now.year, month=now.month, day=now.day)
