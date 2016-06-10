# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='photo',
            field=models.ImageField(upload_to='./upload_images', blank=True, verbose_name='Файл фото'),
        ),
    ]
