# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('height', models.IntegerField(null=True, blank=True, verbose_name='Рост')),
                ('width', models.IntegerField(null=True, blank=True, verbose_name='Вес')),
                ('gender', models.IntegerField(null=True, blank=True, verbose_name='Пол', choices=[(0, 'мужской'), (1, 'женский')])),
                ('training_duration', models.DurationField(null=True, blank=True, verbose_name='Продолжительность тренировок')),
                ('birthday', models.DateField(null=True, blank=True, verbose_name='Дата рождения')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Подтвержден')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='TargetPriority',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(null=True, verbose_name='Наименование', max_length=127)),
                ('priority', models.IntegerField(null=True, verbose_name='Порядок следования приоритетов', unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ZonePriority',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(null=True, verbose_name='Наименование', max_length=127)),
                ('priority', models.IntegerField(null=True, verbose_name='Порядок следования приоритетов', unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
