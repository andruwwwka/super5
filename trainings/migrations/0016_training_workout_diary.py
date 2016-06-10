# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0015_auto_20151013_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='workout_diary',
            field=models.ForeignKey(to='trainings.WorkoutDiary', verbose_name='Дневник тринировки', default=1),
            preserve_default=False,
        ),
    ]
