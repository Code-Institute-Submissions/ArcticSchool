from django.contrib import admin
from .models import QuoteText


class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'description',
    )

    ordering = ('author',)


admin.site.register(QuoteText, QuoteAdmin)
