from django.contrib import admin
from .models import Station, Equipment

# Register your models here.

class StationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'description']
    search_fields = ['name']

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['station', 'name', 'equipment_type']
    search_fields = ['station', 'name']

admin.site.register(Station, StationAdmin)
admin.site.register(Equipment, EquipmentAdmin)