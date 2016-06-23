# coding : utf-8
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def mytest1(request):
    arg = u"I am myTest1..."
    return render(request, 'example1.html', {'arg': arg})


def example_for_loop(request):
    list = ['HTML', "CSS", "jQuery", "python", "Django"]
    return render(request, 'example2.html', {'list': list})
