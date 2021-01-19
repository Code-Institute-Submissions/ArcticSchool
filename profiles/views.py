from django.shortcuts import render


def user_account(request):
    """ A view to return account page """

    return render(request, 'account/account.html')
