# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='tv1'),
    url(r'^example1/', views.example_for_args, name='tv2'),
    url(r'^example2/', views.example_for_loop, name='tv3')
]
