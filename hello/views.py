from django.shortcuts import render, redirect
import re
from datetime import datetime
from django.http import HttpResponse
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView

class HomeListView(ListView):
    """ Renders the home page, with a list of all messages. """
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def hello_there(request, name):   
    return render(request, 'hello/hello_there.html', {'name': name, 'date': datetime.now()})

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})

# Link of this tutorial:
# https://code.visualstudio.com/docs/python/tutorial-django

# Next topic
# Optional activities
