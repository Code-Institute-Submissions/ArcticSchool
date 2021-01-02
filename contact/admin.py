from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'description',
    )

    ordering = ('author',)


admin.site.register(Quote, QuoteAdmin)
