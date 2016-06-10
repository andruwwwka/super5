# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


def add_target(apps, schema_editor):
    Target = apps.get_model('athletes', 'Target')
    db_alias = schema_editor.connection.alias
    Target.objects.using(db_alias).bulk_create(
        [
            Target(name=n)for n in [
                'Повысить энергию',
                'Улучшить мышечный тонус',
                'Похудеть',
                'Улучшить самочувствие',
                'Повысить работоспособность',
            ]
        ]
    )

def add_zone(apps, schema_editor):
    Zone = apps.get_model('athletes', 'Zone')
    db_alias = schema_editor.connection.alias
    Zone.objects.using(db_alias).bulk_create(
        [
            Zone(name=n) for n in [
                'Ноги и ягодицы',
                'Пресс-талия',
                'Спина',
                'Руки',
                'Грудь',
            ]
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('height', models.IntegerField(null=True, blank=True, verbose_name='Рост')),
                ('width', models.IntegerField(null=True, blank=True, verbose_name='Вес')),
                ('gender', models.IntegerField(null=True, choices=[(0, 'мужской'), (1, 'женский')], blank=True, verbose_name='Пол')),
                ('training_duration', models.DurationField(null=True, blank=True, verbose_name='Продолжительность тренировок')),
                ('birthday', models.DateField(null=True, blank=True, verbose_name='Дата рождения')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Подтвержден')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Клиенты',
                'verbose_name': 'Клиент',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, unique=True, max_length=127, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Цели',
                'verbose_name': 'Цель',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(null=True, unique=True, max_length=127, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Целевые зоны',
                'verbose_name': 'Целевая зона',
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='targetpriority',
            options={'verbose_name_plural': 'Приоритет целей', 'verbose_name': 'Приоритет цели'},
        ),
        migrations.AlterModelOptions(
            name='zonepriority',
            options={'verbose_name_plural': 'Приоритет зон', 'verbose_name': 'Приоритет зоны'},
        ),
        migrations.AlterField(
            model_name='targetpriority',
            name='priority',
            field=models.IntegerField(null=True, verbose_name='Приоритет цели'),
        ),
        migrations.AlterField(
            model_name='zonepriority',
            name='priority',
            field=models.IntegerField(null=True, verbose_name='Приоритет'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='targetpriority',
            name='name',
        ),
        migrations.RemoveField(
            model_name='targetpriority',
            name='user',
        ),
        migrations.RemoveField(
            model_name='zonepriority',
            name='name',
        ),
        migrations.RemoveField(
            model_name='zonepriority',
            name='user',
        ),
        migrations.AddField(
            model_name='targetpriority',
            name='athlete',
            field=models.ForeignKey(null=True, to='athletes.Athlete'),
        ),
        migrations.AddField(
            model_name='targetpriority',
            name='target_priority',
            field=models.ForeignKey(null=True, to='athletes.Target'),
        ),
        migrations.AddField(
            model_name='zonepriority',
            name='athlete',
            field=models.ForeignKey(null=True, to='athletes.Athlete'),
        ),
        migrations.AddField(
            model_name='zonepriority',
            name='zone_priority',
            field=models.ForeignKey(null=True, to='athletes.Zone'),
        ),
        migrations.AlterUniqueTogether(
            name='targetpriority',
            unique_together=set([('athlete', 'priority', 'target_priority')]),
        ),
        migrations.AlterUniqueTogether(
            name='zonepriority',
            unique_together=set([('athlete', 'priority', 'zone_priority')]),
        ),
        migrations.RunPython(
            add_target,
        ),
        migrations.RunPython(
            add_zone,
        ),
    ]
