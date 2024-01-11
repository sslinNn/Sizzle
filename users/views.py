from django.shortcuts import render
from .forms import RegisterForm, LoginForm


def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
