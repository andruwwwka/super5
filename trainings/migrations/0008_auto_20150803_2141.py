# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0007_auto_20150802_0029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoexercise',
            options={'verbose_name': 'Сложность упражнения', 'verbose_name_plural': 'Сложность упражнений'},
        ),
    ]
