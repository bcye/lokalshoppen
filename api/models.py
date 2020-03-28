from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import JSONField
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib.gis.db import models as geo_models


class OberKategorie(models.Model):
    slug = models.CharField(max_length=3)
    name = models.CharField(max_length=100)


class UnterKategorie(models.Model):
    slug = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

class Unternehmen(models.Model):
    email = models.EmailField()
    name = models.TextField()
    adresse = models.TextField()
    point = geo_models.PointField(null=True)
    telefon = models.TextField()
    max_pro_slot = models.PositiveSmallIntegerField()
    oeffnungszeiten = JSONField()
    beschreibung = models.TextField()
    active = models.BooleanField(default=False)
    ober_kategorien = models.ManyToManyField(OberKategorie)
    unter_kategorien = models.ManyToManyField(UnterKategorie)


class TimeSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    count = models.PositiveSmallIntegerField(default=0)
    unternehmen = models.ForeignKey(Unternehmen, on_delete=models.CASCADE, null=True)


class Anfrage(models.Model):
    unternehmen = models.ForeignKey(Unternehmen, on_delete=models.CASCADE, null=True)
    kunden_email = models.EmailField()
    text = models.CharField(max_length=500)
    approved = models.BooleanField()
    slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT)

    def save(self, **kwargs):
        if (self.slot.count + 1) > self.unternehmen_id.unternehmensprofil.max_pro_slot or self.slot.day.unternehmen.unternehmensprofil is not self.unternehmen_id.unternehmensprofil:
            raise ValidationError("TimeSlot already filled or wrong slot selected")

        self.slot.count += 1
        self.slot.save()
        return super().save(**kwargs)
