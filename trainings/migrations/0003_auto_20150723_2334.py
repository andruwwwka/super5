# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0002_training_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoexercise',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]
