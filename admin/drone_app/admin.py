from django.contrib import admin
from .models import Drone, ImageData

@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    search_fields = ('name', 'status')

    
@admin.register(ImageData)
class ImageDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'drone', 'timestamp', 'latitude', 'longitude')
    list_filter = ('timestamp',)
    search_fields = ('drone__name', 'latitude', 'longitude')

