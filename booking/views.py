from django.shortcuts import render
from home.models import SocialIcon
from lessons.models import Lesson
import random


def booking(request):
    """ A view to return booking page """

    social = SocialIcon.objects.all()
    lessons = list(Lesson.objects.all())
    random_lessons = random.sample(lessons, 12)

    context = {
        'socials': social,
        'lessons': random_lessons,
    }

    return render(request, 'booking/booking.html', context)
