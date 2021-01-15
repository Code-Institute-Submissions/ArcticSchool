from django.shortcuts import render,redirect, HttpResponse
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


def add_to_booking(request, lesson_id):
    """ Add a quantity of the specified lesson to the booking_bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if lesson_id in list(bag.keys()):
        print('Lesson already exist in bag')
    else:
        bag[lesson_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_booking(request, lesson_id):
    """ Remove lesson from the booking 'bag' """

    try:
        bag = request.session.get('bag', {})
        bag.pop(lesson_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
