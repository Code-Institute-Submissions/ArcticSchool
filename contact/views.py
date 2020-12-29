from django.shortcuts import render
from home.models import SocialIcon


def contact(request):
    """ A view to return contact page """

    social = SocialIcon.objects.all()

    context = {
        'socials': social,
    }

    return render(request, 'contact/contact.html', context)
