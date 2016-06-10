# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0006_auto_20150726_0203'),
        ('trainings', '0008_auto_20150803_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='target',
            field=models.ForeignKey(verbose_name='Тип', blank=True, to='athletes.Target', null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='zone',
            field=models.ForeignKey(verbose_name='Группа мышц', blank=True, to='athletes.Zone', null=True),
        ),
    ]
