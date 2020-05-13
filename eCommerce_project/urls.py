from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main-page-url'),
    path('login/', login_page, name='login-page-url'),
    path('register/', register_page, name='register-page-url'),
    path('products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view())
]