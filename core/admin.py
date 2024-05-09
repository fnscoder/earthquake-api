from django.contrib import admin

from core.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "country", "lat", "long")
    search_fields = ("name", "state", "country")
