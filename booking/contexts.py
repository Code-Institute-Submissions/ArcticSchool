from arctic_school.settings import OFF_10_DISCOUNT_THRESHOLD
from decimal import Decimal
from django.conf import settings


def booking_contents(request):

    booked_lessons = []
    total = 0
    lessons_count = 0

    if total > settings.OFF_10_DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.OFF_10_DISCOUNT/100)
        discount_point = settings.OFF_10_DISCOUNT_THRESHOLD - total
    else:
        discount = 0
        discount_point = 0

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
    }

    return context
