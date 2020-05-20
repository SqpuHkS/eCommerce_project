from .views import *
from django.conf.urls import url

urlpatterns = [
    url('(?P<slug>[\w-]+)/$', ItemDetailSlugView.as_view()),
]