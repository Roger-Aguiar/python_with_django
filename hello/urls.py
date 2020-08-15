# Name:         Roger Silva Santos Aguiar
# Function:     This file is where you specify patterns to route different URLs to their appropriate views.
# Initial date: August 13, 2020
# Last update:  August 13, 2020

# Required modules
from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(queryset=LogMessage.objects.order_by("-log_date")[:5], context_object_name="message_list", template_name="hello/home.html",)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about", views.about, name="about"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("contact", views.contact, name="contact"),
    path("log/", views.log_message, name="log")
]