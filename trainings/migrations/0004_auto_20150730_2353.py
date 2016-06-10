# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0003_auto_20150723_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='place',
        ),
        migrations.RemoveField(
            model_name='training',
            name='slug',
        ),
    ]
