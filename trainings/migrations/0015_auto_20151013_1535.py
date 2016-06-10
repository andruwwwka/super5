# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0014_auto_20150816_0112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DiaryTrainings',
            new_name='WorkoutDiary',
        ),
        migrations.AlterUniqueTogether(
            name='videoexercise',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='videoexercise',
            name='exercise',
        ),
        migrations.AlterModelOptions(
            name='exercise',
            options={'verbose_name': 'Упражнение', 'verbose_name_plural': 'Упражнение'},
        ),
        migrations.RemoveField(
            model_name='training',
            name='diary',
        ),
        migrations.RemoveField(
            model_name='training',
            name='sets',
        ),
        migrations.RemoveField(
            model_name='trainingset',
            name='name',
        ),
        migrations.RemoveField(
            model_name='trainingset',
            name='video_exercise',
        ),
        migrations.AddField(
            model_name='exercise',
            name='difficult',
            field=models.IntegerField(verbose_name='Сложность', default=1),
        ),
        migrations.AddField(
            model_name='exercise',
            name='length',
            field=models.DurationField(verbose_name='Продолжительность', default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='exercise',
            name='synchronous_vimeo_video_link',
            field=models.URLField(verbose_name='Ссылка на синхрон видео на вимео', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='tutorial_vimeo_video_link',
            field=models.URLField(verbose_name='Ссылка на объясняющее видео на вимео', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trainingset',
            name='exercises',
            field=models.ManyToManyField(verbose_name='Упражнения', to='trainings.Exercise'),
        ),
        migrations.AddField(
            model_name='trainingset',
            name='number_in_training',
            field=models.IntegerField(verbose_name='Номер в тренировке', default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='exercise',
            unique_together=set([]),
        ),
        migrations.DeleteModel(
            name='VideoExercise',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='has_been',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='link',
        ),
    ]
