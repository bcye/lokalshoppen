from django.contrib import admin
from .models import Anfrage, TimeSlot, Unternehmen
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
admin.site.register(Anfrage)
admin.site.register(TimeSlot)


@admin.register(Unternehmen)
class UnternehmenAdmin(OSMGeoAdmin):
    default_lat = 6685128
    default_lon = 1138794
    default_zoom = 5
