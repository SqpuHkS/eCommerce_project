from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from .forms import *



def main_page(request):
    if request.user.is_authenticated:
        return render(request, 'main.html', context={'username': request.user.username})
    return render(request, 'main.html')

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html', {'form': form})


def register_page(request):
    User = get_user_model()
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)
    return render(request, 'register.html', context={'form':form})