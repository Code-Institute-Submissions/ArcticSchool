""" Views Lessons App """
import random
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models.functions import Lower
from resorts.models import Resort
from home.models import SocialIcon, LevelCard
from .models import Category, Lesson


def lessons(request):
    """ A view to return lessons in selected category """

    lessons = Lesson.objects.all()
    all_lessons = Lesson.objects.all()
    social = SocialIcon.objects.all()
    categories = Category.objects.all()
    levels = LevelCard.objects.all()

    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                lessons = lessons.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            lessons = lessons.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            lessons = lessons.filter(category__name__in=categories)
            categories = Category.objects.all()

    current_sorting = f'{sort}_{direction}'

    context = {
        'socials': social,
        'lessons': lessons,
        'categories': categories,
        'levels': levels,
        'all_lessons': all_lessons,
        'current_sorting': current_sorting,
    }

    return render(request, 'lessons/lessons.html', context)


def lesson(request, lesson_id):
    """ A view to return lesson detail with resort detail """

    all_lessons = list(Lesson.objects.all())
    resorts = Resort.objects.all()
    social = SocialIcon.objects.all()
    selected_lesson = get_object_or_404(Lesson, pk=lesson_id)
    resort = resorts.get(name=selected_lesson.resort)

    random_lessons = random.sample(all_lessons, 4)

    context = {
        'socials': social,
        'lesson': selected_lesson,
        'resort': resort,
        'lessons': random_lessons,
    }

    return render(request, 'lessons/lesson.html', context)


# Categories Management
@staff_member_required
def categories_management(request):
    """ A view to manage lessons categoires """

    categories = Category.objects.all()
    social = SocialIcon.objects.all()

    template = "lessons/mgmt-categories.html"
    context = {
        'categories': categories,
        'socials': social,
    }

    return render(request, template, context)


@staff_member_required
def add_categories_management(request):
    """ Management view to add lesson category """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def edit_categories_management(request, category_id):
    """ Management view to edit lessons category """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def remove_categories_management(request, category_id):
    """ Management view to remove lessons category """

    category = get_object_or_404(Resort, pk=category_id)
    category.delete()
    messages.success(request, 'Category removed successfully!')

    return redirect(reverse('categories_management'))


# Lessons Management
@staff_member_required
def lessons_management(request):
    """ A view to manage lessons """

    all_lessons = Lesson.objects.all()
    social = SocialIcon.objects.all()

    template = "lessons/mgmt-lessons.html"
    context = {
        'all_lessons': all_lessons,
        'socials': social,
    }

    return render(request, template, context)


@staff_member_required
def add_lessons_management(request):
    """ Management view to add lessons """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def edit_lessons_management(request, lesson_id):
    """ Management view to edit lessons """

    template = "./management/management-forms.html"

    return render(request, template)


@staff_member_required
def remove_lessons_management(request, lesson_id):
    """ Management view to remove lessons """

    lesson = get_object_or_404(Resort, pk=lesson_id)
    lesson.delete()
    messages.success(request, 'Lesson removed successfully!')

    return redirect(reverse('lessons_management'))
