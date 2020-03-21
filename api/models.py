from django.db import models
from django.contrib.auth.models import User
import datetime

class TimeSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()


class Anfrage(models.Model):
    unternehmen = models.ForeignKey(User, on_delete=models.CASCADE)
    kunden_email = models.EmailField()
    text = models.CharField(max_length=500)
    approved = models.BooleanField()
    slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)