from django.contrib import admin
from .models import Resort
# Register your models here.


class ResortsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
        'about',
        'levels',
        'styles',
        'instructors',
    )

    ordering = ('name',)


admin.site.register(Resort, ResortsAdmin)
