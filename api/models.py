from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models as geo_models


class Category(models.Model):
    slug = models.CharField(max_length=3)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class SubCategory(models.Model):
    slug = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "sub categories"


class Company(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)
    address = models.TextField()
    location = geo_models.PointField()
    phone = models.CharField(max_length=30, help_text="Use international format: e.g. +491235565")
    max_per_slot = models.PositiveSmallIntegerField(help_text="Maximum number of persons who can book a particular time slot", default=2)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False, help_text="The company is only listed in the map when this flag is active")

    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    sub_categories = models.ManyToManyField(SubCategory)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies    "


class BusinessHoursWeekday(models.Model):
    WEEKDAYS = (
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    )
    weekday = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    start = models.TimeField()
    end = models.TimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name + ' - ' + self.get_weekday_display()


class TimeSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    company = models.ForeignKey("Company", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if TimeSlot.objects.filter(company=self.company, start=self.start, end=self.end).exists():
            raise ValidationError("TimeSlot exists already, this TimeSlot was not saved...")

        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.company) + ": " + str(self.start) + " - " + str(self.end.time())
    

class Request(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    customer_email = models.EmailField()
    text = models.CharField(max_length=500)
    approved = models.BooleanField(default=False)
    slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if len(Request.objects.filter(slot=self.slot)) > self.company.max_per_slot:
            raise ValidationError("The chosen TimeSlot does not accept anymore requests: " + str(self.slot))

        return super().save(*args, **kwargs)
