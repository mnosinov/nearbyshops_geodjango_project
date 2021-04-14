from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop


class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'address', 'city')


admin.site.register(Shop, ShopAdmin)
