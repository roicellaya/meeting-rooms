# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import MeetingRoomView, RequestReservedView

urlpatterns = [
    url(r'^$', MeetingRoomView.as_view(), name='meeting_room'),
    url(r'^request_reserved/$', RequestReservedView.as_view(),
        name='request_reserved'),
]
