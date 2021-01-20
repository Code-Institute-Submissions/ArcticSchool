from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def user_account(request):
    """ A view to return account page """

    return render(request, 'account/account.html')
