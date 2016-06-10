# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0005_athlete_week_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='week_day',
            field=models.CharField(verbose_name='День недели', null=True, max_length=25),
        ),
    ]
