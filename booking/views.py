from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
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

    lesson = Lesson.objects.get(pk=lesson_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if lesson_id in list(bag.keys()):
        messages.warning(
            request, f'{ lesson.name } already exists in your booking!')
    else:
        bag[lesson_id] = quantity
        messages.success(
            request, f'{ lesson.name } added successfully to your booking!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_booking(request, lesson_id):
    """ Remove lesson from the booking 'bag' """

    try:
        lesson = Lesson.objects.get(pk=lesson_id)
        bag = request.session.get('bag', {})
        bag.pop(lesson_id)

        request.session['bag'] = bag
        messages.error(
            request, f'{ lesson.name } removed successfully from booking!')
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


def clear_booking(request):
    """ A view to clear whole content from booking """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    bag.clear()
    request.session['bag'] = bag

    messages.info(
        request, f'All lessons have been removed from booking successfully!')

    return redirect(redirect_url)
