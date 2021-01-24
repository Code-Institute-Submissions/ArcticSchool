"""
This module will render user account page with
all neccessery user information and forms
"""
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.forms import UserDetailsForm
from home.models import SocialIcon
from checkout.models import Order
from .models import UserProfile


@login_required(login_url='/accounts/login/')
def user_account(request):
    """ A view to return account page """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile detailes updated successfully!')

    details_form = UserDetailsForm(instance=profile)
    orders = profile.orders.all().order_by('-id')[:10]
    social = SocialIcon.objects.all()

    template = 'account/account.html'
    context = {
        'form': details_form,
        'orders': orders,
        'socials': social,
        'no_bag': True,
    }
    return render(request, template, context)


def booking_archived(request, order_number):
    """ A view to return User order history """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def booking_active(request):
    """ A view to return active bookings """

    return render(request, 'profile/account.html')
