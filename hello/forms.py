""" 
Name:         Roger Silva Santos Aguiar
Function:     It defines a Django form that contains field drawn from the data model, LogMessage.
Initial date: August 14, 2020
Last update:  August 14, 2020 """

from django import forms
from hello.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",) # Note: the trailing comma is required.