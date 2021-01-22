"""
This module will render user account page with
all neccessery user information and forms
"""
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.forms import UserDetailsForm
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
    orders = profile.orders.all()

    template = 'account/account.html'
    context = {
        'form': details_form,
        'orders': orders,
        'no_bag': True,
    }
    return render(request, template, context)
