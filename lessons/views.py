from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Lesson
from home.models import SocialIcon, LevelCard
# Create your views here.


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

    print(current_sorting)

    context = {
        'socials': social,
        'lessons': lessons,
        'categories': categories,
        'levels': levels,
        'all_lessons': all_lessons,
        'current_sorting': current_sorting,
    }

    return render(request, 'lessons/lessons.html', context)


def lesson(request, lesson_id, lessons):
    """ A view to return picked lesson detail """

    social = SocialIcon.objects.all()

    context = {
        'socials': social,
        'lessons': lessons,
        'lesson_id': lesson_id,
    }

    return render(request, 'lessons/lesson-detail.html', context)
