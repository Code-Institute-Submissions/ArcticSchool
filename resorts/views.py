from django.shortcuts import render
from .models import Resort
from home.models import SocialIcon
# Create your views here.


def resorts(request):
    """ A view to return team page """

    resorts = Resort.objects.all()
    social =  SocialIcon.objects.all()

    context = {
        'resorts': resorts,
        'socials': social,
    }

    return render(request, 'resorts/resorts.html', context)
