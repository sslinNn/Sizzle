from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import RegisterForm, LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
            else:
                return render(request, 'users/login.html', {'form': form, 'invalid_creds': True})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def user_profile(request):
    return render(request, 'users/profile.html')


def user_register(request):
    form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
