# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0017_remove_exercise_difficult'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingset',
            name='training',
            field=models.ForeignKey(to='trainings.Training', verbose_name='Тренировка', default=1),
            preserve_default=False,
        ),
    ]
