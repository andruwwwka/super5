# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0004_auto_20150730_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название сета', max_length=127, null=True, blank=True)),
                ('exercise', models.ManyToManyField(verbose_name='Упражнения', to='trainings.Exercise', blank=True)),
            ],
            options={
                'verbose_name': 'Сет',
                'verbose_name_plural': 'Сеты',
            },
        ),
        migrations.RemoveField(
            model_name='training',
            name='exercises',
        ),
        migrations.AlterField(
            model_name='training',
            name='diary',
            field=models.ForeignKey(verbose_name='Дневник тринировки', to='trainings.DiaryTrainings'),
        ),
        migrations.AddField(
            model_name='training',
            name='sets',
            field=models.ManyToManyField(verbose_name='Сеты', to='trainings.TrainingSet', blank=True),
        ),
    ]
