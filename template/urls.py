# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='tv1'),
    url(r'^example1/', views.example_for_args, name='tv2'),
    url(r'^example2/', views.example_for_loop, name='tv3'),
    url(r'^example3/', views.example_for_dict, name='tv4'),
    url(r'^example4/', views.example_for_loop_2, name='tv5'),
    url(r'^forms/', views.example_for_form, name='form1')

]
