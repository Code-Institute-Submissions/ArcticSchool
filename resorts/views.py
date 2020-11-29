from django.shortcuts import render
# Create your views here.


def resorts(request):
    """ A view to return team page """

    return render(request, 'resorts/resorts.html')
