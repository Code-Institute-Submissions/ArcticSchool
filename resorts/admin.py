""" This module contains registered Resort Administration """
from django.contrib import admin
from .models import Resort
# Register your models here.


class ResortsAdmin(admin.ModelAdmin):
    """
    Resort app list display in administration
    with ordering
    """
    list_display = (
        'name',
        'country',
        'about',
        'open_season',
        'top_altitude',
        'bottom_altitude',
        'resort_altitude',
        'levels',
        'instructors',
        'image',
    )

    ordering = ('name',)


admin.site.register(Resort, ResortsAdmin)
