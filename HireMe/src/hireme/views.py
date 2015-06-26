from django.shortcuts import render

def homepage(request):
    context = {
        'page_title' : 'Welcome to HireMe!',
    }
    return render(request, 'homepage.html', context)