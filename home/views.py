""" Views for Home App"""
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import LevelCard, LessonCard, SocialIcon


def index(request):
    """ A view to return index page """

    lesson = LessonCard.objects.all()
    levels = LevelCard.objects.all()
    social = SocialIcon.objects.all()

    context = {
        'lessons': lesson,
        'levels': levels,
        'socials': social,
    }

    return render(request, 'home/index.html', context)


@staff_member_required
def lessons_cards_management(request):
    """ A view to manage lessons cards - why our lessons """

    template = "home/mgmt-lessons-cards.html"
    context = {}

    return render(request, template, context)


@staff_member_required
def level_cards_management(request):
    """ A view to manage level cards """

    template = "home/mgmt-level-cards.html"
    context = {}

    return render(request, template, context)


@staff_member_required
def social_media_management(request):
    """ A view to manage social media """

    template = "home/mgmt-social-media.html"
    context = {}

    return render(request, template, context)
