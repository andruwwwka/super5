# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('photo', models.ImageField(upload_to='', verbose_name='Файл фото', blank=True)),
                ('link', models.URLField(verbose_name='Ссылка', blank=True)),
                ('title', models.CharField(max_length=511, verbose_name='Заголовок', blank=True)),
                ('under_title', models.CharField(max_length=511, verbose_name='Подзаголовок', blank=True)),
                ('body', models.TextField(verbose_name='Текст слайда', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Слайды',
                'verbose_name': 'Слайд',
            },
        ),
    ]
