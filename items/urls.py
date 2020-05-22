from .views import *
from django.conf.urls import url

urlpatterns = [
    url('list/', ItemListView.as_view(), name='list'),
    url('(?P<slug>[\w-]+)/$', ItemDetailSlugView.as_view(), name='detail'),
]