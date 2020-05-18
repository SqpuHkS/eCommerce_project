from django.contrib.auth import login, authenticate, get_user_model
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .forms import *
from .models import *



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


class ItemDetailSlugView(DetailView):
    model = Item
    template_name = 'detail.html'

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Item.objects.filter(slug=slug)
        except Item.DoesNotExist:
            raise Http404("Not found...")
        except Item.MultipleObjectsReturned:
            instance = Item.objects.filter(slug=slug).first()
            print(instance)
        return instance

