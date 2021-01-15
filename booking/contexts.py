from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from lessons.models import Lesson


def booking_contents(request):

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

    if total > settings.OFF_10_DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.OFF_10_DISCOUNT/100)
        discount_point = settings.OFF_10_DISCOUNT_THRESHOLD - total
    else:
        discount = 0
        discount_point = settings.OFF_10_DISCOUNT_THRESHOLD - total

    grand_total = total - discount

    context = {
        'booked_lessons': booked_lessons,
        'total': total,
        'lessons_count': lessons_count,
        'discount': discount,
        'discount_point': discount_point,
        'discount_threshold': settings.OFF_10_DISCOUNT_THRESHOLD,
        'discount_percentage': settings.OFF_10_DISCOUNT,
        'grand_total': grand_total,
        'bag': bag,
    }

    return context
