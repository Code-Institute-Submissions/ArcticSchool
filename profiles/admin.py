""" This module contains registered UserProfile administration """
from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """ Administartion display list for user """
    list_display = (
        'user',
        'full_name',
        'email_address',
        'phone_number',
        'street_address1',
        'town_or_city',
        'postcode',
        'country',
        'receiving_newsletter',
    )

    ordering = ('first_name',)


admin.site.register(UserProfile, UserProfileAdmin)
