from django.shortcuts import render
from .models import InstructorProfile
# Create your views here.


def team(request):
    """ A view to return team page """

    instructors = InstructorProfile.objects.all()
    context = {
        'instructors': instructors,
    }

    return render(request, 'team/team.html', context)
