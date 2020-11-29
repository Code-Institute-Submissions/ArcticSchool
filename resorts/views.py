from django.shortcuts import render
from .models import Resort
# Create your views here.


def resorts(request):
    """ A view to return team page """

    resorts = Resort.objects.all()

    context = {
        'resorts': resorts,
    }

    return render(request, 'resorts/resorts.html', context)
