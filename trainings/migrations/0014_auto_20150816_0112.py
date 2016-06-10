# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0013_auto_20150816_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='result',
            field=models.TextField(default='', blank=True, null=True, verbose_name='Результат'),
        ),
    ]
