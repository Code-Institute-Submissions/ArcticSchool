""" A views for Team App """
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from home.models import SocialIcon
from .models import InstructorProfile

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


# Teams Management
@staff_member_required
def instructors_management(request):
    """ A view to manage instructors cards """

    template = "team/mgmt-team.html"
    context = {}

    return render(request, template, context)


@staff_member_required
def add_instructors_management(request):
    """ Management view to add instructor """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def edit_instructors_management(request, instructor_id):
    """ Management view to edit instructor """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def remove_instructors_management(request, instructor_id):
    """ Management view to remove instructor """

    template = "./management/management-forms.html"

    return render(request, template)
