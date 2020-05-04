from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
    path('login/', login_page),
]