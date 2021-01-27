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


# Lessons Card - Why our Lessons? Mangemenet
@staff_member_required
def lessons_cards_management(request):
    """ A view to manage lessons cards - why our lessons """

    template = "home/mgmt-lessons-cards.html"
    context = {}

    return render(request, template, context)


@staff_member_required
def add_lessons_cards_management(request):
    """ Management view to add card """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def edit_lessons_cards_management(request, card_id):
    """ Management view to edit card """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def remove_lessons_cards_management(request, card_id):
    """ Management view to remove card """

    template = "./management/management-forms.html"

    return render(request, template)


# Level Cards Management
@staff_member_required
def level_cards_management(request):
    """ A view to manage level cards """

    template = "home/mgmt-level-cards.html"
    context = {}

    return render(request, template, context)


@staff_member_required
def add_level_cards_management(request):
    """ Management view to add level card """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def edit_level_cards_management(request, level_id):
    """ Management view to edit level card """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def remove_level_cards_management(request, levevl_id):
    """ Management view to remove level card """

    template = "./management/management-forms.html"

    return render(request, template)


# Social Media Management
@staff_member_required
def social_media_management(request):
    """ A view to manage social media """

    social_media = SocialIcon.objects.all()

    template = "home/mgmt-social-media.html"
    context = {
        'socials': social_media,
    }

    return render(request, template, context)


@staff_member_required
def add_social_media_management(request):
    """ Management view to add social media """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def edit_social_media_management(request, social_id):
    """ Management view to edit social media """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def remove_social_media_management(request, social_id):
    """ Management view to remove social media """

    template = "./management/management-forms.html"

    return render(request, template)
