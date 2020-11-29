from django.shortcuts import render
from .models import InstructorProfile
from home.models import SocialIcon
# Create your views here.


def team(request):
    """ A view to return team page """

    instructors = InstructorProfile.objects.all()
    social = SocialIcon.objects.all()

    context = {
        'socials': social,
        'instructors': instructors,
    }

    return render(request, 'team/team.html', context)
