from django.contrib import admin
from .models import Anfrage, TimeSlot

# Register your models here.
admin.site.register(Anfrage)
admin.site.register(TimeSlot)