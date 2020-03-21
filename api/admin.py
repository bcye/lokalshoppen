from django.contrib import admin
from .models import Anfrage, TimeSlot, UnternehmensProfil

# Register your models here.
admin.site.register(Anfrage)
admin.site.register(TimeSlot)
admin.site.register(UnternehmensProfil)