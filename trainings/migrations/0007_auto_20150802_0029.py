# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0006_exercise_has_been'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingset',
            name='exercise',
        ),
        migrations.AddField(
            model_name='exercise',
            name='link',
            field=models.URLField(blank=True, verbose_name='Ссылка  на видео'),
        ),
        migrations.AddField(
            model_name='trainingset',
            name='video_exercise',
            field=models.ManyToManyField(blank=True, verbose_name='Упражнения', to='trainings.VideoExercise'),
        ),
    ]
