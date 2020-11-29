from django.contrib import admin
from .models import Resort
# Register your models here.


class ResortsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
        'address',
        'about',
        'levels',
        'styles',
        'instructors',
        'map_link',
        'image_url',
        'image',
    )

    ordering = ('name',)


admin.site.register(Resort, ResortsAdmin)
