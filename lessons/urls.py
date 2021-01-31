""" Lessons App URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('<lesson_id>', views.lesson, name='lesson'),
    # Management Categories  Url's
    path('management/lessons-page/categories',
         views.categories_management, name='categories_management'),
    path('management/lessons-page/categories/add',
         views.add_categories_management, name='add_categories_management'),
    path('management/lessons-page/categories/edit/<int:category_id>',
         views.edit_categories_management, name='edit_categories_management'),
    path('management/lessons-page/categories/remove/<int:category_id>',
         views.remove_categories_management, name='remove_categories_management'),
    # Management Lessons Url's
    path('management/lessons-page/lessons',
         views.lessons_management, name='lessons_management'),
    path('management/lessons-page/lessons/add',
         views.add_lessons_management, name='add_lessons_management'),
    path('management/lessons-page/lessons/edit<int:lesson_id>',
         views.edit_lessons_management, name='edit_lessons_management'),
    path('management/lessons-page/lessons/remove/<int:lesson_id>',
         views.remove_lessons_management, name='remove_lessons_management'),
]
