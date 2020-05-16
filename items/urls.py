from .views import *
from django.conf.urls import url

urlpatterns = [
    url('login/', login_page, name='login-page-url'),
    url('register/', register_page, name='register-page-url'),
    url('items/(?P<slug>[\w-]+)/$', ItemDetailSlugView.as_view()),
    url('', main_page, name='main-page-url'),
]