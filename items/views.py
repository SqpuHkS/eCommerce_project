from django.contrib.auth import login, authenticate, get_user_model
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import *
from .models import *



class ItemListView(ListView):
    model = Item
    template_name = 'items/list.html'


class ItemDetailSlugView(DetailView):
    model = Item
    template_name = 'items/detail.html'

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Item.objects.filter(slug=slug)
        except Item.DoesNotExist:
            raise Http404("Not found...")
        except Item.MultipleObjectsReturned:
            instance = Item.objects.filter(slug=slug).first()
        return instance

