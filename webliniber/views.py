from django.shortcuts import render


def index(request):
    context = {
        'title': ''
    }
    return render(request, 'webliniber/index.html', context)


def animales(request):
    context = {}
    return render(request, 'webliniber/animales.html', context)
