from django.shortcuts import render
from .models import Category, Lesson
# Create your views here.


def lessons(request):
    """ A view to return lessons page """

    categories = Category.objects.all()
    lessons = Category.objects.all()

    context = {
        'categories': categories,
        'lessons': lessons
    }

    return render(request, 'lessons/lessons.html', context)
