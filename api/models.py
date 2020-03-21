from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Anfrage(models.Model):
    unternehmen = models.ForeignKey(User, on_delete=models.CASCADE)
    kunden_email = models.EmailField()
    text = models.CharField(max_length=500)
    start_datum = models.DateTimeField()
    end_datum = models.DateTimeField()
    approved = models.BooleanField()