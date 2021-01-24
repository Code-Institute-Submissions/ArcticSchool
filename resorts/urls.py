""" Url paths for Resorts App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.resorts, name='resorts'),
]
