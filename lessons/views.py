from django.shortcuts import render
# Create your views here.


def lessons(request):
    """ A view to return lessons page """

    context = {
    }

    return render(request, 'lessons/lessons.html', context)
