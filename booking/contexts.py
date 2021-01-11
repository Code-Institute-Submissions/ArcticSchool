from decimal import Decimal
from django.conf import settings


def booking_contents(request):


    booked_lessons = []
    total = 0
    lessons_count = 0

    if total < 200:
        total_cost = total * Decimal(settings.OFF_10_DISCOUNT)

    context = {}

    return context
