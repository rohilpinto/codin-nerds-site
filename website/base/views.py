from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'base/index.html', context)


def about(request):
    context = {}
    return render(request, 'base/about.html', context)
