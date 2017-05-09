# -*- coding: utf-8 -*-
from django.contrib import admin
# Register your models here.
from models import Equipment, MeetingRoom

admin.site.register(Equipment)
admin.site.register(MeetingRoom)
