# coding: utf-8
from django import forms

class CalcForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
