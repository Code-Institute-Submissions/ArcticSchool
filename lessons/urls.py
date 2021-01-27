""" Url paths for Lessons App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('<lesson_id>', views.lesson, name='lesson'),
    path('management/lessons-page/categories',
         views.categories_management, name='categories_management'),
    path('management/lessons-page/lessons',
         views.lessons_management, name='lessons_management'),
]
