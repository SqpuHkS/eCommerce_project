from django.conf.urls import url

from .views import *


urlpatterns = [

    url('payment-method/$', payment_method_view, name='payment-method'),
    url('payment-method/create/$', payment_method_create_view, name='payment-method-endpoint'),

]

app_name = 'billing'
