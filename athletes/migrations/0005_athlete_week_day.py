# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0004_auto_20150724_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='week_day',
            field=models.CharField(max_length=25, unique=True, verbose_name='День недели', null=True),
        ),
    ]
