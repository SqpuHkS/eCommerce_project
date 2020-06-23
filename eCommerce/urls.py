"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from items.views import *
from carts.views import *
from eCommerce.views import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url('login/', login_page, name='login-page-url'),
    url('carts/', cart_home, name='carts-url'),
    url('register/', register_page, name='register-page-url'),
    url('items/', include('items.urls', namespace='items')),
    url('search/', include('search.urls', namespace='search')),
    url('^$', main_page, name='main-page-url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
