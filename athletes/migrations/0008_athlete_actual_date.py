# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0007_auto_20150803_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='actual_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата изменения данных'),
        ),
    ]
