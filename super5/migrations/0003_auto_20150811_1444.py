# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super5', '0002_auto_20150809_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='photo',
            field=models.ImageField(verbose_name='Файл фото', blank=True, upload_to='./media/upload_images'),
        ),
    ]
