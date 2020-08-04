from .views import *
from django.conf.urls import url
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url('^login/$', login_page, name='login'),
    url('^register/$', register_page, name='register'),
    url('^logout/$', LogoutView.as_view(), name='logout'),
]

app_name = 'accounts'