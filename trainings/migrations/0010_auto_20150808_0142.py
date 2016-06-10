# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0009_auto_20150803_2207'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='videoexercise',
            unique_together=set([('difficult', 'exercise')]),
        ),
    ]
