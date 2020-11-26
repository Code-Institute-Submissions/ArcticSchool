from django.shortcuts import render

# Create your views here.


def team(request):
    """ A view to return team page """
    return render(request, 'team/team.html')
