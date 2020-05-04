from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import *



def main_page(request):
    return render(request, 'main.html')

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect('/')
    return render(request, 'login.html', {'form': form})

def register_page(request):
    return render(request, 'register.html')