""" Contact App URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
]
