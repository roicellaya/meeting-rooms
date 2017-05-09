# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-09 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Equipment',
                'verbose_name_plural': 'Equipments',
            },
        ),
        migrations.AlterModelOptions(
            name='meetingroom',
            options={'verbose_name': 'MeetingRoom', 'verbose_name_plural': 'MeetingRooms'},
        ),
    ]