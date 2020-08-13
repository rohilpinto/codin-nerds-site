from django.shortcuts import render


def resources_show(request):
    context = {}
    return render(request, 'materials/resources.html', context)


def tools_show(request):
    context = {}
    return render(request, 'materials/tools.html', context)


def help_show(request):
    context = {}
    return render(request, 'materials/help.html', context)
