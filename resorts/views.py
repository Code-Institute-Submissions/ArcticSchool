""" Views for Resorts App """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from home.models import SocialIcon
from resorts.forms import ResortForm
from .models import Resort


def resorts(request):
    """ A view to return resorts page """

    all_resorts = Resort.objects.all()
    social = SocialIcon.objects.all()

    context = {
        'resorts': all_resorts,
        'socials': social,
    }

    return render(request, 'resorts/resorts.html', context)


# Resorts Management
@staff_member_required
def resorts_management(request):
    """ A view to manage resorts """

    all_resorts = Resort.objects.all()
    social = SocialIcon.objects.all()

    template = "resorts/mgmt-resorts.html"
    context = {
        'resorts': all_resorts,
        'socials': social,
    }

    return render(request, template, context)


@staff_member_required
def add_resorts_management(request):
    """ Management view to add resort """

    if request.method == 'POST':
        form = ResortForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resort added successfully!')
            return redirect(reverse('resorts_management'))
        else:
            messages.error(
                request, 'Adding new resort failed. Please ensure the form is valid.')
    else:
        form = ResortForm()

    template = "./management/management-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_resorts_management(request, resort_id):
    """ Management view to edit resort """

    resort = get_object_or_404(Resort, pk=resort_id)
    if request.method == 'POST':
        form = ResortForm(request.POST, request.FILES, instance=resort)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Resort edited successfully!')
            return redirect(reverse('resorts_management'))
        else:
            messages.error(
                request, 'Editing Resort failed. \
                Please ensure the form is valid.')
    else:
        form = ResortForm(instance=resort)

    template = "./management/management-forms.html"
    context = {
        'form': form,
        'resort': resort,
    }

    return render(request, template, context)


@staff_member_required
def remove_resorts_management(request, resort_id):
    """ Management view to remove resort """

    resort = get_object_or_404(Resort, pk=resort_id)
    if resort.image:
        resort.image.delete()
        resort.delete()
    else:
        resort.delete()
    messages.success(request, 'Resort removed successfully!')

    return redirect(reverse('resorts_management'))
