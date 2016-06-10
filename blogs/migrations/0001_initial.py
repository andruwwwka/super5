# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('head', models.CharField(verbose_name='Заголовок поста', max_length=255)),
                ('body', redactor.fields.RedactorField(verbose_name='Тело поста')),
                ('post_date', models.DateTimeField(verbose_name='Дата поста')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
            ],
            options={
                'verbose_name_plural': 'Посты',
                'verbose_name': 'Пост',
            },
        ),
    ]
