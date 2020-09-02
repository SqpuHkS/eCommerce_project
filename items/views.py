from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from analytics.mixins import AnalyticMixin
from carts.models import Cart

from .models import *



class ItemListView(ListView):
    model = Item
    template_name = 'items/list.html'


class ItemDetailSlugView(AnalyticMixin, DetailView):
    model = Item
    template_name = 'items/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailSlugView, self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('slug')

        try:
            instance = Item.objects.filter(slug=slug)
        except Item.DoesNotExist:
            raise Http404("Not found...")
        except Item.MultipleObjectsReturned:
            instance = Item.objects.filter(slug=slug).first()

        return instance

