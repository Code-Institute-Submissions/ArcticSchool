from django.shortcuts import render, redirect
from home.models import SocialIcon
from lessons.models import Lesson
import random


def booking(request):
    """ A view to return booking page """

    social = SocialIcon.objects.all()
    lessons = list(Lesson.objects.all())
    random_lessons = random.sample(lessons, 12)

    if 'bag' in request.session:
        bag = request.session.get('bag')
        print( bag )
    else:
        bag = []

    context = {
        'socials': social,
        'lessons': random_lessons,
        'bag':bag,
    }

    return render(request, 'booking/booking.html', context)


def add_to_booking(request, lesson_id):
    """ Add a quantity of the specified lesson to the booking_bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if lesson_id in list(bag.keys()):
        print('Lesson already in bag')
    else:
        bag[lesson_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return render(request, 'booking/booking.html')