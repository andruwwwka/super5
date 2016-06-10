# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_athlete_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='training_duration',
            field=models.IntegerField(verbose_name='Продолжительность тренировок', null=True, blank=True, choices=[(0, '5 минут'), (1, '15 минут'), (2, '30 минут'), (3, '60 минут')]),
        ),
    ]
