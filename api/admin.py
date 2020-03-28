from django.contrib import admin
from .models import Anfrage, TimeSlot, Unternehmen, OberKategorie, UnterKategorie
from django.contrib.gis.admin import OSMGeoAdmin

class KategorieAdmin(admin.ModelAdmin):
    list_display = ("slug", "name")
    search_fields = ("name", "slug")

# Register your models here.
admin.site.register(Anfrage)
admin.site.register(TimeSlot)
admin.site.register(OberKategorie, KategorieAdmin)
admin.site.register(UnterKategorie, KategorieAdmin)


@admin.register(Unternehmen)
class UnternehmenAdmin(OSMGeoAdmin):
    default_lat = 6685128
    default_lon = 1138794
    default_zoom = 5

    search_fields = ("name", "email", "telefon")
    list_display = ("name", "email", "telefon")
    autocomplete_fields = ("ober_kategorien", "unter_kategorien")

