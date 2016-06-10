# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0012_auto_20150808_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='result',
            field=models.TextField(default='', verbose_name='Результат', blank=True),
        ),
    ]
