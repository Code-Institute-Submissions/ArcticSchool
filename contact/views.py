import random
from django.db.models import query
from django.shortcuts import render
from .models import QuoteText


def contact(request):
    """ A view to return contact page and quotes """
    quote = list(QuoteText.objects.all())
    quote = random.sample(quote, 1)
    quote = random.choice(quote)

    context = {
        'quote': quote,
    }

    return render(request, 'contact/contact.html', context)
