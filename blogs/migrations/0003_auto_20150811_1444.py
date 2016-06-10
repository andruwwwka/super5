# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20150809_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(verbose_name='Фото для главной страницы (опционально)', blank=True, null=True, upload_to='./media/upload_images'),
        ),
    ]
