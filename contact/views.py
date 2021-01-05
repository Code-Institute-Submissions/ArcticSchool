from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            from_email = contact_form.cleaned_data['from_email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [
                          from_email, settings.EMAIL_HOST_USER], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Dear ' + name.capitalize() + ', thanks for reaching out!')
    return render(request, "contact/contact.html", {'contact_form': contact_form})