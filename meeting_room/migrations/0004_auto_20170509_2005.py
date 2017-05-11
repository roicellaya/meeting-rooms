# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-09 23:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_room', '0003_equipos_iniciales'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AlterModelOptions(
            name='meetingroom',
            options={'verbose_name': 'Sala de reuni\xf3n', 'verbose_name_plural': 'Sala de reuniones'},
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(default='', max_length=200, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='availability_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Disponible hasta'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='availability_start',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Disponible desde'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='capacity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Capacidad'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='location',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Ubicaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='status',
            field=models.CharField(choices=[('available', 'Disponible'), ('not_available', 'No Disponible'), ('reserved', 'Reservada'), ('confirmed', 'Confirmada')], default='available', max_length=50, verbose_name='Estado'),
        ),
    ]