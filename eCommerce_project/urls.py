from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', main_page, name='main-page-url'),
    path('login/', login_page, name='login-page-url'),
    path('register/', register_page, name='register-page-url'),
    url('items/(?P<slug>[\w-]+)/$', ItemDetailSlugView.as_view())
]