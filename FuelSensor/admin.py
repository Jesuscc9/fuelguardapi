from django.contrib import admin

from .models import Alert, FuelData, FuelHistory, FuelSensor, Geofence, Truck

admin.site.register(Truck)
admin.site.register(FuelSensor)
admin.site.register(FuelData)
admin.site.register(Alert)
admin.site.register(Geofence)
admin.site.register(FuelHistory)
