from django.shortcuts import render
from .models import Lesson, Levels, Social

# Create your views here.


def index(request):
    """ A view to return index page """

    lesson = Lesson.objects.all()
    levels = Levels.objects.all()
    social = Social.objects.all()

    context = {
        'lessons': lesson,
        'levels': levels,
        'socials': social,
    }

    return render(request, 'home/index.html', context)
