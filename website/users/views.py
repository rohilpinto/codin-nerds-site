from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('site-home')
        else:
            messages.info(request, "Username or Password is incorrect!")

    context = {
    }
    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout()
    return redirect('login')
