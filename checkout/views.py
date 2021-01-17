from django.conf import settings
from django.shortcuts import redirect, render, reverse
from django.contrib import messages

from checkout.forms import OrderForm
from home.models import SocialIcon
from booking.contexts import booking_contents

import stripe


def checkout(request):
    public_key = settings.STRIPE_PUBLIC_KEY
    secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.info(request, "Your booking is empty")
        return redirect(reverse('lessons'))

    currnet_bag = booking_contents(request)
    total = currnet_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not public_key:
        messages.warning(
            request, 'Stripe public key is missing. Check your environment, maybe it is there sleeping.')

    template = 'checkout/checkout.html'
    social = SocialIcon.objects.all()

    context = {
        'order_form': order_form,
        'socials': social,
        'stripe_public_key': public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
