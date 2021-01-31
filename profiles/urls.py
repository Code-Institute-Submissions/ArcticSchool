""" Profiles App URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_account, name='user_account'),
    path('booking/review/<order_number>',
         views.booking_review, name='booking_review'),
    path('bookings/active', views.bookings_active, name='bookings_active'),
    path('bookings/archived', views.bookings_archived, name='bookings_archived'),
]
