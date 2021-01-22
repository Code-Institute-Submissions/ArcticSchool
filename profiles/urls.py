""" This module contains urls for profiles app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_account, name='user_account'),
]
