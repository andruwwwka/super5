# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_notice_type(apps, schema_editor):
    NoticeType = apps.get_model('notifications', 'NoticeType')
    db_alias = schema_editor.connection.alias
    NoticeType.objects.using(db_alias).get_or_create(
        label='registration',
        display='Регистрация в Super5',
        description='Поздравляем, Вы успешно зарегистрировались в Super5',
        default=2
    )

class Migration(migrations.Migration):

    dependencies = [
        ('extend_notifications', '0001_initial'),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_notice_type,
        ),
    ]
