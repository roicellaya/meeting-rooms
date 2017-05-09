# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class MeetingRoom(models.Model):
    AVAILABLE = 'available'
    NOT_AVAILABLE = 'not_available'
    RESERVED = 'reserved'
    CONFIRMED = 'confirmed'

    ROOM_STATUS = (
        (AVAILABLE, _('RoomAvailable')),
        (NOT_AVAILABLE, _('RoomNotAvailable')),
        (RESERVED, _('RoomReserved')),
        (CONFIRMED, _('RoomConfirmed')),
    )

    name = models.CharField(max_length=200, null=False, blank=False)
    location = models.CharField(
        max_length=200, default=None, blank=True, null=True
    )
    capacity = models.IntegerField(null=True, blank=True)
    availability_start = models.DateTimeField(default=datetime.now)
    availability_end = models.DateTimeField(default=datetime.now)
    status = models.CharField(
        max_length=50, choices=ROOM_STATUS,
        default=AVAILABLE, null=False, blank=False
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = _('MeetingRoom')
        verbose_name_plural = _('MeetingRooms')

    def __unicode__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(
        max_length=200, null=False, blank=False, default=''
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = _('Equipment')
        verbose_name_plural = _('Equipments')

    def __unicode__(self):
        return self.name
