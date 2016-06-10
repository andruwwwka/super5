# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_video_xercises(apps, schema_editor):
    data_for_save = [
        ('legs', 'energy', 'Fitness 115(sin)', 'Fitness 115(sin) video','https://vimeo.com/135348631'),
        ('legs', 'tone', 'Fitness 111(sin)', 'Fitness 111(sin) video','https://vimeo.com/135348630'),
        ('legs', 'weight loss', 'Fitness 114(sin)', 'Fitness 114(sin)video','https://vimeo.com/135348158'),
        ('legs', 'health', 'Fitness 111', 'Fitness 111 video','https://vimeo.com/135348157'),
        ('legs', 'plastic', 'Fitness 115', 'Fitness 115 video','https://vimeo.com/135348156'),
        ('abdominal', 'energy', 'Fitness 118(sin)', 'Fitness 118(sin) video','https://vimeo.com/135347816'),
        ('abdominal', 'tone', 'Fitness 116', 'Fitness 116 video','https://vimeo.com/135347297'),
        ('abdominal', 'weight loss', 'Fitness 116(sin)', 'Fitness 116(sin) video','https://vimeo.com/135347296'),
        ('abdominal', 'health', 'Fitness 117(sin)', 'Fitness 117(sin) video','https://vimeo.com/135347295'),
        ('abdominal', 'plastic', 'Fitness 156', 'Fitness 156 video','https://vimeo.com/135347292'),
        ('back', 'energy', 'Fitness 167', 'Fitness 167 video','https://vimeo.com/135346615'),
        ('back', 'tone', 'Fitness 168(sin)', 'Fitness 168(sin) video','https://vimeo.com/135346614'),
        ('back', 'weight loss', 'Fitness 170(sin)', 'Fitness 170(sin) video','https://vimeo.com/135346613'),
        ('back', 'health', 'Fitness 174', 'Fitness 174 video','https://vimeo.com/135346611'),
        ('back', 'plastic', 'Fitness 197', 'Fitness 197 video','https://vimeo.com/135346610'),
        ('arms', 'energy', 'Fitness 262', 'Fitness 262 video','https://vimeo.com/135345379'),
        ('arms', 'tone', 'Fitness 259', 'Fitness 259 video','https://vimeo.com/135345380'),
        ('arms', 'weight loss', 'Fitness 258(sin)', 'Fitness 258(sin) video','https://vimeo.com/135345885'),
        ('arms', 'health', 'Fitness 258', 'Fitness 258 video','https://vimeo.com/135345886'),
        ('arms', 'plastic', 'Fitness 257(sin left)', 'Fitness 257(sin left) video','https://vimeo.com/135345887'),
        ('pectoral', 'energy', 'Fitness 249(sin left)', 'Fitness 249(sin left) video','https://vimeo.com/135345888'),
        ('pectoral', 'tone', 'Fitness 248(sin left)', 'Fitness 248(sin left) video','https://vimeo.com/135345889'),
        ('pectoral', 'weight loss', 'Fitness 245(sin right)', 'Fitness 245(sin right) video','https://vimeo.com/135346212'),
        ('pectoral', 'health', 'Fitness 277', 'Fitness 277 video','https://vimeo.com/135345376'),
        ('pectoral', 'plastic', 'Fitness 276', 'Fitness 276 video','https://vimeo.com/135345377'),
    ]
    db_alias = schema_editor.connection.alias
    Zone = apps.get_model('athletes', 'Zone')
    Target = apps.get_model('athletes', 'Target')
    Exercise = apps.get_model('trainings', 'Exercise')
    VideoExercise = apps.get_model('trainings', 'VideoExercise')
    for zone, target, name, desc, link in data_for_save:
        zone_obj = Zone.objects.using(db_alias).get(slug=zone)
        target_obj = Target.objects.using(db_alias).get(slug=target)
        exerc = Exercise(
            title=name,
            description=desc,
            link=link,
            zone=zone_obj,
            target=target_obj
        )
        exerc.save()
        video_exerc = VideoExercise(
            exercise=exerc,
            description=desc,
            link=link,
            difficult=0
        )
        video_exerc.save()


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0010_auto_20150808_0142'),
    ]

    operations = [
        migrations.RunPython(
            add_video_xercises,
        ),
    ]
