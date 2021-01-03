import random
from django.db.models import query
from django.shortcuts import render
from .models import QuoteText


def contact(request):
    """ A view to return contact page and quotes """

    return render(request, 'contact/contact.html')
