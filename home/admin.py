""" App registered in Administration from Home page """
from django.contrib import admin
from .models import LevelCard, LessonCard, SocialIcon


class LevelsAdmin(admin.ModelAdmin):
    """ Levels Card admin list display and ordering """
    list_display = (
        'title',
        'level',
        'description',
    )

    ordering = ('level',)


class LessonsAdmin(admin.ModelAdmin):
    """ Lessons Card admin list display and ordering """
    list_display = (
        'title',
        'description',
    )

    ordering = ('title',)


class SocialsAdmin(admin.ModelAdmin):
    """ Social Media Icons admin list display and ordering """
    list_display = (
        'name',
        'icon',
        'url',
    )

    ordering = ('name',)


admin.site.register(LevelCard, LevelsAdmin)
admin.site.register(LessonCard, LessonsAdmin)
admin.site.register(SocialIcon, SocialsAdmin)
