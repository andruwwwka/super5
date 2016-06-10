# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_added_zone_target_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='level',
            field=models.IntegerField(null=True, blank=True, choices=[(0, 'низкий'), (1, 'ниже среднего'), (2, 'средний'), (3, 'высокий'), (4, 'очень высокий')], verbose_name='Уровень подготовки'),
        ),
    ]
