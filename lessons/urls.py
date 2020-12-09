from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('<category_name>', views.category_result, name='category_result')
]