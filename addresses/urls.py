from .views import *
from django.conf.urls import url

urlpatterns = [
    url('^create/', checkout_address_create_view, name='create'),

]

app_name = 'address'