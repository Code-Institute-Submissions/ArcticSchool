""" Views Lessons App """
import random
from django.shortcuts import render, get_object_or_404
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


def categories_management(request):
    """ A view to manage lessons categoires """

    template = "lessons/mgmt-categories.html"
    context = {}

    return render(request, template, context)


def lessons_management(request):
    """ A view to manage lessons """

    template = "lessons/mgmt-lessons.html"
    context = {}

    return render(request, template, context)
