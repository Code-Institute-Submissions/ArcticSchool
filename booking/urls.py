from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('add/<lesson_id>', views.add_to_booking, name='add_to_booking'),
    path('remove/<lesson_id>', views.remove_from_booking,
         name='remove_from_booking'),
]
