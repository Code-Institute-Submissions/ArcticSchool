from django.shortcuts import render
from home.models import SocialIcon


def booking(request):
    """ A view to return booking page """

    social = SocialIcon.objects.all()

    context = {
        'socials': social,
    }

    return render(request, 'booking/booking.html', context)