# coding: utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^p1/', views.example1, name='push_1'),
]
