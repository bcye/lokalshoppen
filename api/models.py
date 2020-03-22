from django.db import models
from django.contrib.auth.models import User


class TimeSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()


class Anfrage(models.Model):
    unternehmen_id = models.ForeignKey(User, on_delete=models.CASCADE)
    kunden_email = models.EmailField()
    text = models.CharField(max_length=500)
    approved = models.BooleanField()
    slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)


class UnternehmensProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    adresse = models.TextField()
    langitude = models.TextField()
    longitude = models.TextField()
    telefon = models.TextField()
    max_pro_slot = models.PositiveSmallIntegerField()
    oeffnungszeiten = models.TextField()
    available_time_slots = models.TextField()
    beschreibung = models.TextField()

    # Kategorien
    KATEGORIEN_CHOICES = [
        ("LEB", "Lebensmittel"),
        ("BAE", "Bäckerei"),
        ("FLE", "Fleischerei"),
        ("GET", "Getränke"),
        ("DRO", "Drogerie"),
        ("ELE", "Elektronik"),
        ("HWO", "Haushalt & Wohnen"),
        ("WEB", "Werkeln & Basteln"),
        ("SPO", "Sport"),
        ("UNT", "Unterhaltung"),
        ("MOD", "Mode"),
        ("APO", "Apotheke"),
        ("KIO", "Zeitungen & Kiosk"),
    ]
    ober_kategorie = models.CharField(max_length=3, choices=KATEGORIEN_CHOICES)
    unter_kategorien = models.TextField()
