from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact(request):

    if request.method == "GET":

        contact_from = ContactForm()
        template = 'contact/contact.html'

        context = {
            'contact_form': contact_from,
        }

        return render(request, template, context)
