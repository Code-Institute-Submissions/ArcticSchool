""" Url paths for Resorts App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.resorts, name='resorts'),
    path('management/resorts-page/resorts',
         views.resorts_management, name='resorts_management'),
]
