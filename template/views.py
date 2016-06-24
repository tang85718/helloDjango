# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalcForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def example_for_args(request):
    arg = u"I am myTest1..."
    return render(request, 'example1.html', {'arg': arg})


def example_for_loop(request):
    list = ['HTML', "CSS", "jQuery", "python", "Django"]
    return render(request, 'example2.html', {'list': list})


def example_for_dict(request):
    info_dict = {'site': '自强学院', 'content': '爬虫技术教程'}
    return render(request, 'example3.html', {"info_dict": info_dict})


def example_for_loop_2(request):
    list = map(str, range(100))
    return render(request, 'example4.html', {'list': list})


def example_for_form(request):
    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = CalcForm()
    return render(request, 'exampleForm.html', {'form': form})
