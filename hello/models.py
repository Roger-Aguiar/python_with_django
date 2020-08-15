""" 
Name:         Roger Silva Santos Aguiar
Function:     It defines all the required models
Initial date: August 14, 2020
Last update:  August 14, 2020 
"""

from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField('date logged')

    def __str__(self):
        """ Returns a string representation of a message. """
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

