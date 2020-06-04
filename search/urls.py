from .views import *
from django.conf.urls import url

urlpatterns = [
    url('^$', SearchItemView.as_view(), name='search-list')
]

app_name = 'search'