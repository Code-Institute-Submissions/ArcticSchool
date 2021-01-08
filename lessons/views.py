from resorts.models import Resort
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from .models import Category, Lesson
from resorts.models import Resort
from home.models import SocialIcon, LevelCard


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

    lessons = Lesson.objects.all()
    resorts = Resort.objects.all()
    social = SocialIcon.objects.all()
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    resort = resorts.get(name=lesson.resort)

    context = {
        'socials': social,
        'lesson': lesson,
        'resort': resort,
        'lessons':lessons,
    }

    return render(request, 'lessons/lesson.html', context)
