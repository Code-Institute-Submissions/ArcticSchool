""" Apps registered in Administration from Team App """
from django.contrib import admin
from .models import InstructorProfile

# Register your models here.


class InstructorProfileAdmin(admin.ModelAdmin):
    """ Instructor Profiles admin list display and ordering """
    list_display = (
        'name',
        'age',
        'about',
    )

    ordering = ('name',)


admin.site.register(InstructorProfile, InstructorProfileAdmin)
