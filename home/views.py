""" Views for Home App"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from home.forms import LessonCardsForm, LevelCardsForm, SocialMediaIconsForm
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

    social_media = SocialIcon.objects.all()
    our_lessons_cards = LessonCard.objects.all()

    template = "home/mgmt-lessons-cards.html"
    context = {
        'socials': social_media,
        'our_lessons_cards': our_lessons_cards,
    }

    return render(request, template, context)


@staff_member_required
def add_lessons_cards_management(request):
    """ Management view to add card """

    if request.method == 'POST':
        form = LessonCardsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Why Our Lesson Card added successfully!')
            return redirect(reverse('lessons_cards_management'))
        else:
            messages.error(
                request, 'Adding Why Our Lesson Card failed. Please ensure the form is valid.')
    else:
        form = LessonCardsForm()

    template = "./management/management-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_lessons_cards_management(request, card_id):
    """ Management view to edit card """

    card = get_object_or_404(LessonCard, pk=card_id)
    if request.method == 'POST':
        form = LessonCardsForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Why Our Lesson Card edited successfully!')
            return redirect(reverse('lessons_cards_management'))
        else:
            messages.error(
                request, 'Editing Why Our Lesson Card failed. \
                Please ensure the form is valid.')
    else:
        form = LessonCardsForm(instance=card)

    template = "./management/management-forms.html"
    context = {
        'form': form,
        'card': card,
    }

    return render(request, template, context)


@staff_member_required
def remove_lessons_cards_management(request, card_id):
    """ Management view to remove card """

    lesson_card = get_object_or_404(LessonCard, pk=card_id)
    lesson_card.delete()
    messages.success(request, 'Why Our Lessons Card removed successfully!')

    return redirect(reverse('lessons_cards_management'))


# Level Cards Management
@staff_member_required
def level_cards_management(request):
    """ A view to manage level cards """

    social_media = SocialIcon.objects.all()
    level_cards = LevelCard.objects.all()

    template = "home/mgmt-level-cards.html"
    context = {
        'socials': social_media,
        'level_cards': level_cards,
    }

    return render(request, template, context)


@staff_member_required
def add_level_cards_management(request):
    """ Management view to add level card """

    if request.method == 'POST':
        form = LevelCardsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Level Card added successfully!')
            return redirect(reverse('level_cards_management'))
        else:
            messages.error(
                request, 'Adding Level Card failed. Please ensure the form is valid.')
    else:
        form = LevelCardsForm()

    template = "./management/management-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_level_cards_management(request, level_id):
    """ Management view to edit level card """

    level = get_object_or_404(LevelCard, pk=level_id)
    if request.method == 'POST':
        form = LevelCardsForm(request.POST, request.FILES, instance=level)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Level Card edited successfully!')
            return redirect(reverse('level_cards_management'))
        else:
            messages.error(
                request, 'Editing Level Card failed. \
                Please ensure the form is valid.')
    else:
        form = LevelCardsForm(instance=level)

    template = "./management/management-forms.html"
    context = {
        'form': form,
        'level': level,
    }

    return render(request, template, context)


@staff_member_required
def remove_level_cards_management(request, level_id):
    """ Management view to remove level card """

    level_card = get_object_or_404(LevelCard, pk=level_id)
    level_card.delete()
    messages.success(request, 'Level Card removed successfully!')

    return redirect(reverse('level_cards_management'))


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

    if request.method == 'POST':
        form = SocialMediaIconsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social Media Icon added successfully!')
            return redirect(reverse('social_media_management'))
        else:
            messages.error(
                request, 'Adding new social media icon faild. Please ensure the form is valid.')
    else:
        form = SocialMediaIconsForm()

    template = "./management/management-forms.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required
def edit_social_media_management(request, social_id):
    """ Management view to edit social media """

    social = get_object_or_404(SocialIcon, pk=social_id)
    if request.method == 'POST':
        form = SocialMediaIconsForm(request.POST, instance=social)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Social media icon edited successfully!')
            return redirect(reverse('social_media_management'))
        else:
            messages.error(
                request, 'Editing social media icon failed. \
                Please ensure the form is valid.')
    else:
        form = SocialMediaIconsForm(instance=social)

    template = "./management/management-forms.html"
    context = {
        'form': form,
        'social': social,
    }

    return render(request, template, context)


@staff_member_required
def remove_social_media_management(request, social_id):
    """ Management view to remove social media """

    social_media_icon = get_object_or_404(SocialIcon, pk=social_id)
    social_media_icon.delete()
    messages.success(request, 'Social media icon removed successfully!')

    return redirect(reverse('social_media_management'))
