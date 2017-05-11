# -*- coding: utf-8 -*-
from datetime import date
from models import Equipment, MeetingRoom, Reservation
from django import forms
from django.utils.translation import ugettext as _


class ReservationForm(forms.ModelForm):
    room = forms.ModelChoiceField(
        label=_('Room'),
        queryset=MeetingRoom.objects.filter(status=MeetingRoom.AVAILABLE),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    num_people = forms.IntegerField(
        label=_('NumPeople'), required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    equipments = forms.ModelMultipleChoiceField(
        label=_('Equipments'),
        widget=forms.CheckboxSelectMultiple(),
        queryset=Equipment.objects.all(),
        required=False
    )
    date = forms.DateField(
        label=_('Date'), required=True,
        widget=forms.TextInput(attrs={'class': 'form-control datepicker'}),
        initial=date.today()
    )
    start_hour = forms.TimeField(
        label=_('StartHour'), required=True,
        widget=forms.TextInput(attrs={'class': 'form-control timepicker'})
    )
    end_hour = forms.TimeField(
        label=_('EndHour'), required=True,
        widget=forms.TextInput(attrs={'class': 'form-control timepicker'})
    )

    def clean_num_people(self):
        room = self.cleaned_data.get('room')
        if self.cleaned_data.get('num_people') > room.capacity:
            raise forms.ValidationError(_('CapacityExceeded'))
        return self.cleaned_data.get('num_people')

    def clean_start_hour(self):
        start_hour = self.cleaned_data.get('start_hour')
        room = self.cleaned_data.get('room')
        if start_hour < room.availability_start:
            raise forms.ValidationError(_('ReservEarly'))
        return self.cleaned_data.get('start_hour')

    def clean_end_hour(self):
        end_hour = self.cleaned_data.get('end_hour')
        room = self.cleaned_data.get('room')

        if room.availability_end is not None:
            if end_hour > room.availability_end:
                raise forms.ValidationError(_('ReservLate'))
        return self.cleaned_data.get('end_hour')

    def clean(self):
        cleaned_data = super(ReservationForm, self).clean()
        start_hour = cleaned_data.get('start_hour')
        end_hour = cleaned_data.get('end_hour')

        if start_hour and end_hour:
            if start_hour >= end_hour:
                raise forms.ValidationError(_('HoursMustDiffer'))

    class Meta:
        model = Reservation
        fields = ['room', 'date', 'num_people',
            'equipments', 'start_hour', 'end_hour'
        ]
