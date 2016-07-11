# coding: utf-8
from django import forms


class MessageForm(forms.Form):
    title = forms.CharField()
