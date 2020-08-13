# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Welcome to Codin\' Nerds Official Website!</h1>')


def about(request):
    return HttpResponse('<h1>About Codin\' Nerds</h1>')
