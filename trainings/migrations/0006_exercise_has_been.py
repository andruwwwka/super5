# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0005_auto_20150731_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='has_been',
            field=models.BooleanField(default=False, verbose_name='Упражнение знакомо клиенту'),
        ),
    ]
