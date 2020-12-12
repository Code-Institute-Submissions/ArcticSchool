from django.shortcuts import render, get_object_or_404
from .models import Category, Lesson
from home.models import SocialIcon
# Create your views here.


def lessons(request):
    """ A view to return lessons page - categories """

    categories = Category.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, 'lessons/lessons.html', context)


def category_result(request, category_name):
    """ A view to return lessons in selected category """

    lessons = Lesson.objects.all()
    social = SocialIcon.objects.all()

    if category_name == "all_lessons":
        lessons = lessons
    else:
        lessons = lessons.filter(category__name=category_name)

    context = {
        'socials': social,
        'lessons': lessons,
        'category_name': category_name,
    }

    return render(request, 'lessons/lessons-category-page.html', context)


def lesson(request, lesson_id, lessons):
    """ A view to return picked lesson detail """

    social = SocialIcon.objects.all()

    context = {
        'socials': social,
        'lessons': lessons,
        'lesson_id': lesson_id,
    }

    return render(request, 'lessons/lesson-detail.html', context)

