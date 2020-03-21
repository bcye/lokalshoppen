from django.db import models
from django.contrib.auth.models import User
import datetime

class TimeSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()


class Anfrage(models.Model):
    unternehmen_id = models.ForeignKey(User, on_delete=models.CASCADE)
    kunden_email = models.EmailField()
    text = models.CharField(max_length=500)
    approved = models.BooleanField()
    slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)


class UnternehmenProfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    adresse = models.TextField()
    langitude = models.TextField()
    longitude = models.TextField()
    telefon = models.TextField()
    max_pro_slot = models.PositiveSmallIntegerField()
