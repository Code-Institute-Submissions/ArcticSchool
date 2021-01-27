""" Url paths for Team App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name='team'),
    path('management/team-page/instructors',
         views.instructors_management, name='instructors_management'),
]
