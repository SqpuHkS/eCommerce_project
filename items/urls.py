from .views import *
from django.conf.urls import url

urlpatterns = [
    url('list/', ItemListView.as_view()),
    url('(?P<slug>[\w-]+)/$', ItemDetailSlugView.as_view()),
]