from django.contrib import admin
from django.urls import  include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from items.views import *
from carts.views import *
from eCommerce.views import *
from billing.views import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url('account/', include('accounts.urls', namespace='account')),
    url('cart/', include('carts.urls', namespace='cart')),
    url('items/', include('items.urls', namespace='items')),
    url('search/', include('search.urls', namespace='search')),
    url('api/cart/', cart_detail_api_view, name='cart-api'),
    url('billing/payment-method', payment_method_view, name='payment-method'),
    url('checkout/address/', include('addresses.urls', namespace='address')),
    url('^$', main_page, name='main-page-url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
