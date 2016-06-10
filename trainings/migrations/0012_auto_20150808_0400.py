# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0011_auto_20150808_0209'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='exercise',
            unique_together=set([('zone', 'target')]),
        ),
    ]
