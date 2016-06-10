# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0019_auto_20151013_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingset',
            name='length_of_every_exercise',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='difficulty',
            field=models.IntegerField(verbose_name='Сложность', null=True, blank=True, choices=[(0, 'Низкий'), (1, 'Ниже среднего'), (2, 'Средний'), (3, 'Высокий'), (4, 'Очень высокий')]),
        ),
    ]
