""" Url paths for Resorts App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.resorts, name='resorts'),
    # Management Resort Url's
    path('management/resorts-page/resorts',
         views.resorts_management, name='resorts_management'),
    path('management/resorts-page/resorts/add',
         views.add_resorts_management, name='add_resorts_management'),
    path('management/resorts-page/resorts/edit/<int:resort_id>',
         views.edit_resorts_management, name='edit_resorts_management'),
    path('management/resorts-page/resorts/remove/<int:resort_id>',
         views.remove_resorts_management, name='remove_resorts_management'),
]
