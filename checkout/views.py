from checkout.forms import OrderForm
from django.conf import settings
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from home.models import SocialIcon


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.info(request, "Your booking is empty")
        return redirect(reverse('lessons'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    social = SocialIcon.objects.all()
    public_key = settings.STRIPE_PUBLIC_KEY
    secret_key = settings.STRIPE_SECRET_KEY

    context = {
        'order_form': order_form,
        'socials': social,
        'stripe_public_key': public_key,
        'client_secret': secret_key,
    }

    return render(request, template, context)
