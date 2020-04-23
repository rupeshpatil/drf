from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^employees/$', views.UserCreate.as_view(), name='employees'),

]