from django.db import models

# Create your models here
class Appointment(models.Model):
    anfrage = models.CharField(max_length=240)
    zeit = models.DateTimeField()
    laenge = models.PositiveIntegerField()