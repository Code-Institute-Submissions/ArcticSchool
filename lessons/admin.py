from django.contrib import admin
from .models import Category, Lesson


class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

    ordering = ('name',)


class LessonsAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'start_date',
        'end_date',
        'start_time',
        'end_time',
        'participants',
        'place',
        'price'
    )

    ordering = ('name',)


admin.site.register(Category, CategoriesAdmin)
admin.site.register(Lesson, LessonsAdmin)
