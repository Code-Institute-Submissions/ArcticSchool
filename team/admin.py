from django.contrib import admin
from .models import InstructorProfile

# Register your models here.


class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'about',
        'image_url',
        'image',
    )

    ordering = ('name',)


admin.site.register(InstructorProfile, InstructorProfileAdmin)
