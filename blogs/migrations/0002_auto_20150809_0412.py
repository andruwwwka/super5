# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_main',
            field=models.CharField(max_length=511, blank=True, null=True, verbose_name='Текст для главной страницы (опционально)'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='./upload_images', blank=True, null=True, verbose_name='Фото для главной страницы (опционально)'),
        ),
        migrations.AddField(
            model_name='post',
            name='show_in_feed',
            field=models.BooleanField(default=False, verbose_name='Показывать в основной ленте блога'),
        ),
        migrations.AddField(
            model_name='post',
            name='show_in_main',
            field=models.BooleanField(default=False, verbose_name='Показывать на главной странице'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_main',
            field=models.CharField(max_length=511, blank=True, null=True, verbose_name='Заголовок для главной страницы (опционально)'),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на видео (опционально)'),
        ),
    ]
