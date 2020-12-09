from django.shortcuts import render, get_object_or_404
from .models import Category, Lesson
# Create your views here.


def lessons(request):
    """ A view to return lessons page """

    categories = Category.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, 'lessons/lessons.html', context)


def category_result(request, category_name):

    lessons = Lesson.objects.all()
    lessons = lessons.filter(category__name=category_name)

    context = {
        'lessons': lessons,
        'category_name': category_name,
    }

    return render(request, 'lessons/lessons-cat.html', context)
