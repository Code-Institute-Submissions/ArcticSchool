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
    """ Management view to add instructor card """

    if request.method == 'POST':
        form = InstructorProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Instructor Profile card added successfully!')
            return redirect(reverse('instructors_management'))
        else:
            messages.error(
                request, 'Adding new Instructor Profile Card failed. \
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
    """ Management view to edit instructor card """

    instructor = get_object_or_404(InstructorProfile, pk=instructor_id)
    if request.method == 'POST':
        form = InstructorProfileForm(
            request.POST, request.FILES, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Instructor Profile Card edited successfully!')
            return redirect(reverse('instructors_management'))
        else:
            messages.error(
                request, 'Editing Instructor Profile card failed. \
                Please ensure the form is valid.')
    else:
        form = InstructorProfileForm(instance=instructor)

    template = "./management/management-forms.html"
    context = {
        'form': form,
        'instructor': instructor,
    }

    return render(request, template, context)


@staff_member_required
def remove_instructors_management(request, instructor_id):
    """ Management view to remove instructor card """

    instructor_profile = get_object_or_404(InstructorProfile,  pk=instructor_id)
    if instructor_profile.image:
        instructor_profile.image.delete()
        instructor_profile.delete()
    else:
        instructor_profile.delete()
    messages.success(request, 'Instructor Card removed successfully!')

    return redirect(reverse('instructors_management'))
