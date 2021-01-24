""" Booking bag content """
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from lessons.models import Lesson


def booking_contents(request):
    """
    This function will allow to use booking
    contents 'bag' on whole application
    """

    booked_lessons = []
    total = 0
    lessons_count = 0
    bag = request.session.get('bag', {})

    for lesson_id, quantity in bag.items():
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        total += quantity * lesson.price
        lessons_count += quantity
        booked_lessons.append({
            'lesson_id': lesson_id,
            'quantity': quantity,
            'lesson': lesson,
        })

    if total > settings.OFF_DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.OFF_DISCOUNT/100)
        discount_point = settings.OFF_DISCOUNT_THRESHOLD - total
    else:
        discount = 0
        discount_point = settings.OFF_DISCOUNT_THRESHOLD - total

    grand_total = total - discount

    context = {
        'booked_lessons': booked_lessons,
        'total': total,
        'lessons_count': lessons_count,
        'discount': discount,
        'discount_point': discount_point,
        'discount_threshold': settings.OFF_DISCOUNT_THRESHOLD,
        'discount_percentage': settings.OFF_DISCOUNT,
        'grand_total': grand_total,
        'bag': bag,
    }

    return context
