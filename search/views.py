from django.db.models import Q
from django.views.generic.list import ListView
from items.models import *

# Create your views here.

class SearchItemView(ListView):
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        # the lane bellow give to the context variable all the data that context
        # had before we override it
        context = super(SearchItemView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        q = request.GET.get('q')
        # q is a search symbol since the url start to read your searching sentence
        # like http://localhost:8000/search/?q=hat
        if q is not None:
            return Item.search(self, q)
        return Item.objects.featured()