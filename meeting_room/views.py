# -*- coding: utf-8 -*-
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.views import View
from forms import ReservationForm
from models import MeetingRoom


class MeetingRoomView(LoginRequiredMixin, View):
    """Vista para manejar los get y post de reservas de salas"""
    template_name = 'meeting_room/meeting_rooms.html'
    login_url='/login/'

    def dispatch(self, *args, **kwargs):
        return super(MeetingRoomView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Se construye el formulario
        form = ReservationForm()
        reserved_rooms = MeetingRoom.objects.filter(status=MeetingRoom.RESERVED)
        unavailable_rooms = MeetingRoom.objects.filter(
            Q(status=MeetingRoom.NOT_AVAILABLE) |
            Q(status=MeetingRoom.CONFIRMED)
        )

        return render(
            request, self.template_name,
            {
                'form': form,
                'reserveds': reserved_rooms,
                'unavailables': unavailable_rooms
            }
        )

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)
        reserved_rooms = MeetingRoom.objects.filter(status=MeetingRoom.RESERVED)
        unavailable_rooms = MeetingRoom.objects.filter(
            Q(status=MeetingRoom.NOT_AVAILABLE) |
            Q(status=MeetingRoom.CONFIRMED)
        )

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            # Se cambia el estatus de la sala a reservada
            reservation.room.status = MeetingRoom.RESERVED
            reservation.room.save()

            reservation.save()

            messages.success(request, _('ReservationSuccess'))

        return render(
            request, self.template_name,
            {
                'form': form,
                'reserved': reserved_rooms,
                'unavailables': unavailable_rooms
            }
        )


class RequestReservedView(LoginRequiredMixin, View):
    """Vista para solicitar una sala reservada"""
    template_name = 'meeting_room/meeting_rooms.html'
    login_url='/login/'

    def dispatch(self, *args, **kwargs):
        return super(RequestReservedView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = ReservationForm()
        reserved_rooms = MeetingRoom.objects.filter(status=MeetingRoom.RESERVED)
        unavailable_rooms = MeetingRoom.objects.filter(
            Q(status=MeetingRoom.NOT_AVAILABLE) |
            Q(status=MeetingRoom.CONFIRMED)
        )

        messages.info(request, _('EmailServiceUnavailable'))

        return render(
            request, self.template_name,
            {
                'form': form,
                'reserved': reserved_rooms,
                'unavailables': unavailable_rooms
            }
        )
