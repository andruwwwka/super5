# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0018_trainingset_training'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='length',
        ),
        migrations.AddField(
            model_name='exercise',
            name='difficulty',
            field=models.IntegerField(blank=True, null=True, verbose_name='Группа мышц', choices=[(0, 'Низкий'), (1, 'Ниже среднего'), (2, 'Средний'), (3, 'Высокий'), (4, 'Очень высокий')]),
        ),
        migrations.AddField(
            model_name='trainingset',
            name='length_of_every_exercise',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='Продолжительность каждого упражнения'),
        ),
    ]
