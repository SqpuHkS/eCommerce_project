from .views import *
from django.conf.urls import url

urlpatterns = [
    url('^$', SearchProductView.as_view(), name='search-list')
]

app_name = 'search'