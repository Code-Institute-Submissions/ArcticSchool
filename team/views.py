""" A views for Team App """
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from home.models import SocialIcon
from team.forms import InstructorProfileForm
from .models import InstructorProfile


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

    instructors = InstructorProfile.objects.all()
    social = SocialIcon.objects.all()

    template = "team/mgmt-team.html"
    context = {
        'instructors': instructors,
        'socials': social,
    }

    return render(request, template, context)


@staff_member_required
def add_instructors_management(request):
    """ Management view to add instructor """

    if request.method == 'POST':
        form = InstructorProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Instructor profile card added uccessfully!')
            return redirect(reverse('instructors_management'))
        else:
            messages.error(
                request, 'Adding new Instructor profile card faild. \
                Please ensure the form is valid.')
    else:
        form = InstructorProfileForm()

    template = "./management/management-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_instructors_management(request, instructor_id):
    """ Management view to edit instructor """

    instructor = get_object_or_404(InstructorProfile, pk=instructor_id)
    social = SocialIcon.objects.all()
    template = "./management/management-forms.html"

    context = {
        'instructor': instructor,
        'socials': social,
    }

    return render(request, template, context)


@staff_member_required
def remove_instructors_management(request, instructor_id):
    """ Management view to remove instructor """

    instructor_profile = get_object_or_404(InstructorProfile, pk=instructor_id)
    instructor_profile.delete()
    messages.success(request, 'Instructor card removed successfully!')

    return redirect(reverse('instructors_management'))
