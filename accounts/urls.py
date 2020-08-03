from .views import *
from django.conf.urls import url

urlpatterns = [
    url('^login/$', login_page, name='login'),
    url('^register/$', register_page, name='register'),
]

app_name = 'accounts'