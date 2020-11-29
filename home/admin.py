from django.contrib import admin
from .models import LevelCard, LessonCard, SocialIcon
# Register your models here.

class LevelsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'level',
        'description',
    )

    ordering = ('level',)

class LessonsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
    )

    ordering = ('title',)

class SocialsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'icon',
        'url',
    )

    ordering = ('title',)

admin.site.register(LevelCard, LevelsAdmin)
admin.site.register(LessonCard, LessonsAdmin)
admin.site.register(SocialIcon, SocialsAdmin)