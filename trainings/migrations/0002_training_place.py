# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='place',
            field=models.IntegerField(choices=[(0, 'Зал'), (1, 'Дом')], verbose_name='Место проведения тренировки', default=0),
        ),
    ]
