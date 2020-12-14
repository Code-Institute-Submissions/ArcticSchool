from django.shortcuts import render, get_object_or_404
from .models import Category, Lesson
from home.models import SocialIcon, LevelCard
# Create your views here.


def lessons(request):
    """ A view to return lessons in selected category """

    lessons = Lesson.objects.all()
    social = SocialIcon.objects.all()
    categories = Category.objects.all()
    levels = LevelCard.objects.all()

    context = {
        'socials': social,
        'lessons': lessons,
        'categories': categories,
        'levels': levels,
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
