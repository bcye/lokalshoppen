from django.contrib import admin
from .models import Request, TimeSlot, Company, Category, SubCategory, BusinessHours
from django.contrib.gis.admin import OSMGeoAdmin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("slug", "name")
    search_fields = ("name", "slug")

class RequestAdmin(admin.ModelAdmin):
    list_display = ("company", "customer_email", "slot")

# Register your models here.
admin.site.register(Request, RequestAdmin)
admin.site.register(TimeSlot)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, CategoryAdmin)
admin.site.register(BusinessHours)


@admin.register(Company)
class CompanyAdmin(OSMGeoAdmin):
    default_lat = 6685128
    default_lon = 1138794
    default_zoom = 5

    search_fields = ("name", "email", "phone")
    list_display = ("name", "email", "phone")
    autocomplete_fields = ("category", "sub_categories")

