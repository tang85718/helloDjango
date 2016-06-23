#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 100)
    c = int(a) + int(b)
    return HttpResponse(u'计算结果=%s' % str(c))


def add_for_grace(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(u'优雅网址计算方法:%s' % str(c))