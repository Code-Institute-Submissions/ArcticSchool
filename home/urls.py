""" Url paths for Home App """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # Management Lessons Cards Media Url's
    path('management/home-page/lessons-cards',
         views.lessons_cards_management, name='lessons_cards_management'),
    path('management/home-page/lessons-cards/add',
         views.add_lessons_cards_management, name='add_lessons_cards_management'),
    path('management/home-page/lessons-cards/edit/<int:card_id>',
         views.edit_lessons_cards_management, name='edit_lessons_cards_management'),
    path('management/home-page/lessons-cards/remove/<int:card_id>',
         views.remove_lessons_cards_management, name='remove_lessons_cards_management'),
    # Management Level Cards Url's
    path('management/home-page/level-cards',
         views.level_cards_management, name='level_cards_management'),
    path('management/home-page/level-cards/add',
         views.add_level_cards_management, name='add_level_cards_management'),
    path('management/home-page/level-cards/edit/<int:level_id>',
         views.edit_level_cards_management, name='edit_level_cards_management'),
    path('management/home-page/level-cards/remove/<int:level_id>',
         views.remove_level_cards_management, name='remove_level_cards_management'),
    # Management Social Media Url's
    path('management/home-page/social-media',
         views.social_media_management, name='social_media_management'),
    path('management/home-page/social-media/add',
         views.add_social_media_management, name='add_social_media_management'),\
    path('management/home-page/social-media/edit/<int:social_id>',
         views.edit_social_media_management, name='edit_social_media_management'),
    path('management/home-page/social-media/remove/<int:social_id>',
         views.remove_social_media_management, name='remove_social_media_management'),

]
