# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryTrainings',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Дневник тренировок',
                'verbose_name_plural': 'Дневники тренировок',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='Название', default='')),
                ('description', models.TextField(verbose_name='Описание', default='')),
            ],
            options={
                'verbose_name': 'Упражнение',
                'verbose_name_plural': 'Упражнения',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField(verbose_name='Дата', default=django.utils.timezone.now)),
                ('slug', models.SlugField(unique=True)),
                ('result', models.TextField(verbose_name='Результат', default='')),
                ('diary', models.ForeignKey(to='trainings.DiaryTrainings')),
                ('exercises', models.ManyToManyField(to='trainings.Exercise', blank=True)),
            ],
            options={
                'verbose_name': 'Тренировка',
                'verbose_name_plural': 'Тренировки',
            },
        ),
        migrations.CreateModel(
            name='VideoExercise',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('link', models.URLField(verbose_name='Ссылка  на видео')),
                ('difficult', models.IntegerField(verbose_name='Сложность', default=1)),
                ('length', models.DurationField(verbose_name='Продолжительность', default=datetime.timedelta(0))),
                ('description', models.TextField(default='')),
                ('exercise', models.ForeignKey(null=True, to='trainings.Exercise')),
            ],
            options={
                'verbose_name': 'Видео упражнения',
                'verbose_name_plural': 'Видео упражнений',
            },
        ),
    ]
