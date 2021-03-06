# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-10 20:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meeting_room', '0004_auto_20170509_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('start_hour', models.TimeField(verbose_name='Hora de inicio')),
                ('end_hour', models.TimeField(verbose_name='Hora de fin')),
                ('num_people', models.IntegerField(verbose_name='Asistentes')),
                ('equipments', models.CharField(max_length=512, verbose_name='Equipos')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='meeting_room.MeetingRoom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
        ),
    ]
