from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
    )

    ordering = ('first_name',)


admin.site.register(UserProfile, UserProfileAdmin)