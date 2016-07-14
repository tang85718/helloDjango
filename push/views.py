from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import MessageForm


# Create your views here.


def example1(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            messages.add_message(request, messages.INFO, title)
            return render(request, 'push/push1.html', {'form': form})
    else:
        form = MessageForm()

    return render(request, 'push/push1.html', {'form': form})
