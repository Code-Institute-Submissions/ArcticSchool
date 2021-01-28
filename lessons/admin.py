""" Administration settings for Lessons App """
from django.contrib import admin
from .models import Category, Lesson


class CategoriesAdmin(admin.ModelAdmin):
    """ Lesson categories list display with order """
    list_display = (
        'name',
        'friendly_name',
    )

    ordering = ('name',)


class LessonsAdmin(admin.ModelAdmin):
    """ Lessons list display and order """
    list_display = (
        'name',
        'category',
        'level',
        'resort',
        'participants',
        'start_date',
        'end_date',
        'start_time',
        'end_time',
        'price',
    )

    ordering = ('name',)


admin.site.register(Category, CategoriesAdmin)
admin.site.register(Lesson, LessonsAdmin)
