""" Url paths for Team App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name='team'),
    # Management Teams Url's
    path('management/team-page/instructors',
         views.instructors_management, name='instructors_management'),
    path('management/team-page/instructors/add',
         views.add_instructors_management, name='add_nstructors_management'),
    path('management/team-page/instructors/edit/<int:instructor_id>',
         views.edit_instructors_management, name='edit_instructors_management'),
    path('management/team-page/instructors/remove/<int:instructor_id>',
         views.remove_instructors_management, name='remove_instructors_management'),
]
