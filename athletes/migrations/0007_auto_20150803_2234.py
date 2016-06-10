# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_target_slug(apps, schema_editor):
    Target = apps.get_model('athletes', 'Target')
    db_alias = schema_editor.connection.alias
    slugs = [
        ('Повысить энергию', 'energy'),
        ('Улучшить мышечный тонус', 'tone'),
        ('Похудеть', 'weight loss'),
        ('Улучшить самочувствие', 'health'),
        ('Повысить работоспособность', 'plastic'),
    ]
    for name, slug in slugs:
        target = Target.objects.using(db_alias).get(name=name)
        target.slug = slug
        target.save()

def add_zone_slug(apps, schema_editor):
    Zone = apps.get_model('athletes', 'Zone')
    db_alias = schema_editor.connection.alias
    slugs = [
        ('Ноги и ягодицы', 'legs'),
        ('Пресс-талия', 'abdominal'),
        ('Спина', 'back'),
        ('Руки', 'arms'),
        ('Грудь', 'pectoral'),
    ]
    for name, slug in slugs:
        zone = Zone.objects.using(db_alias).get(name=name)
        zone.slug = slug
        zone.save()


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0006_auto_20150726_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Идентификатор типа тренировок'),
        ),
        migrations.AddField(
            model_name='zone',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Идентификатор группы мышц'),
        ),
        migrations.RunPython(
            add_target_slug,
        ),
        migrations.RunPython(
            add_zone_slug,
        ),
    ]
