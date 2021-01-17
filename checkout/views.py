from checkout.forms import OrderForm
from django.shortcuts import redirect, render, reverse
from django.contrib import messages


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your booking is empty")
        return redirect(reverse('lessons'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,

    }

    return render(request, template, context)
