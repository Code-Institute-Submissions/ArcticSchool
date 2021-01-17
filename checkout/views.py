from checkout.forms import OrderForm
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

    context = {
        'order_form': order_form,
        'socials':social,

    }

    return render(request, template, context)
