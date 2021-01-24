""" Url paths for Lessons App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('<lesson_id>', views.lesson, name='lesson'),
]
