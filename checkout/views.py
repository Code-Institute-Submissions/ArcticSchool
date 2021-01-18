from django.conf import settings
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages

from checkout.forms import OrderForm
from checkout.models import Order, OrderLineItem
from lessons.models import Lesson
from home.models import SocialIcon
from booking.contexts import booking_contents

import stripe


def checkout(request):
    public_key = settings.STRIPE_PUBLIC_KEY
    secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for lesson_id, item_data in bag.items():
                try:
                    lesson = Lesson.objects.get(id=lesson_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            lesson=lesson,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        messages.error("Something whent wrong..")

                except Lesson.DoesNotExist:
                    messages.error(request, (
                        "One of the lessons in your booking 'bag' wasn't found in our database. "
                        "Please message us for assistance!"
                    ))
                order.delete()
                return redirect(reverse('booking'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout-success', args=[order.order_number]))

        else:
            messages.error(request, "There was an error with your form. \
                Check your information, please.")

    else:
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
            request, 'Stripe public key is missing. \
                Check your environment, maybe it is there sleeping.')

    template = 'checkout/checkout.html'
    social = SocialIcon.objects.all()

    context = {
        'order_form': order_form,
        'socials': social,
        'stripe_public_key': public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ A view to render succesfull checkouts """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. Check your email and confirmation \
        we have sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
