""" This module contains urls for profiles app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_account, name='user_account'),
    path('bookings/archived/<order_number>',
         views.booking_archived, name='booking_archived'),
    path('bookings/active/<order_number>',
         views.booking_active, name='booking_active'),
]
