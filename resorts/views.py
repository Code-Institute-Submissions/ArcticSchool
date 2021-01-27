""" Views for Resorts App """
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from home.models import SocialIcon
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


@staff_member_required
def resorts_management(request):
    """ A view to manage resorts """

    template = "resorts/mgmt-resorts.html"
    context = {}

    return render(request, template, context)
