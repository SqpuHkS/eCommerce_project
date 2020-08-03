from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^$', cart_home, name='home'),
    url('^update/$', cart_update, name='update'),
    url('^checkout/$', checkout_home, name='checkout'),
]

app_name = 'cart'