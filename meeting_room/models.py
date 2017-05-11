# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class MeetingRoom(models.Model):
    """
    Description: Clase usada para registrar una sala de reuniones
    """
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

    name = models.CharField(_('Name'), max_length=200, null=False, blank=False)
    location = models.CharField(
        _('Location'), max_length=200,
        default=None, blank=True, null=True
    )
    capacity = models.IntegerField(_('Capacity'), null=True, blank=True)
    availability_start = models.TimeField(
        _('AvailabilityStart'), null=True, blank=True
    )
    availability_end = models.TimeField(
        _('AvailabilityEnd'), null=True, blank=True
    )
    status = models.CharField(
        _('Status'), max_length=50, choices=ROOM_STATUS,
        default=AVAILABLE, null=False, blank=False
    )
    created = models.DateTimeField(
        _('Created'), auto_now_add=True, editable=False
    )
    updated = models.DateTimeField(_('Updated'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('MeetingRoom')
        verbose_name_plural = _('MeetingRooms')

    def __unicode__(self):
        return self.name


class Equipment(models.Model):
    """
    Description: Clase usada para registrar equipos usados
                 en las salas de reuniones
    """
    name = models.CharField(
        _('Name'), max_length=200, null=False,
        blank=False, default='', unique=True
    )
    created = models.DateTimeField(
        _('Created'), auto_now_add=True, editable=False
    )
    updated = models.DateTimeField(_('Updated'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('Equipment')
        verbose_name_plural = _('Equipments')

    def __unicode__(self):
        return self.name


class Reservation(models.Model):
    """
    Description: Clase usada para registrar las reservas
    """
    user = models.ForeignKey(User, related_name='reservations')
    room = models.ForeignKey(MeetingRoom, related_name='reservations')
    date = models.DateField(_('Date'), null=False, blank=False)
    start_hour = models.TimeField(_('StartHour'), null=False, blank=False)
    end_hour = models.TimeField(_('EndHour'), null=False, blank=False)
    num_people = models.IntegerField(_('NumPeople'), null=False, blank=False)
    equipments = models.CharField(
        _('Equipments'), max_length=512, null=True, blank=True
    )

    class Meta:
        verbose_name = _('Reservation')
        verbose_name_plural = _('Reservations')

    def __unicode__(self):
        return self.user.username + ', ' + self.room.name
