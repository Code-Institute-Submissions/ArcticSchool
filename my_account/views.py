from django.shortcuts import render

# Create your views here.
def my_account(request):
    """ A view to return my account page """
    return render(request, 'my_account/login-register.html')