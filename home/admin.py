from django.contrib import admin
from .models import Levels, Lesson, Social
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

admin.site.register(Levels, LevelsAdmin)
admin.site.register(Lesson, LessonsAdmin)
admin.site.register(Social, SocialsAdmin)