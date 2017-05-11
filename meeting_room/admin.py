# -*- coding: utf-8 -*-
from django.contrib import admin
# Register your models here.
from models import Equipment, MeetingRoom, Reservation


class MeetingRoomAdmin(admin.ModelAdmin):
	list_display = ('name', 'location', 'capacity', 'availability_start',
		'availability_end', 'status', 'created', 'updated')
	list_filter = ('status', 'capacity')
	search_fields = ('name', 'location', 'capacity')


class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'created', 'updated')
	search_fields = ('name',)


class ReservationAdmin(admin.ModelAdmin):
	list_display = ('user', 'room', 'date', 'start_hour',
		'end_hour', 'num_people', 'equipments')
	list_filter = ('room', 'num_people')
	search_fields = ('user', 'room', 'num_people', 'equipments')
	readonly_fields = ('user', 'room')

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(MeetingRoom, MeetingRoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
