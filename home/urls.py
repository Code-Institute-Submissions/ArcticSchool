""" Url paths for Home App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('management/home-page/lessons-cards',
         views.lessons_cards_management, name='lessons_cards_management'),
    path('management/home-page/level-cards',
         views.level_cards_management, name='level_cards_management'),
    path('management/home-page/social-media',
         views.social_media_management, name='social_media_management'),

]
