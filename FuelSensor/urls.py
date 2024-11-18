from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TruckViewSet, FuelSensorViewSet, FuelDataViewSet,
    AlertViewSet, GeofenceViewSet, FuelHistoryViewSet
)

app_name = 'FuelSensor'

# Configuración del router
router = DefaultRouter()
router.register(r'trucks', TruckViewSet, basename='truck')
router.register(r'fuel-sensors', FuelSensorViewSet, basename='fuel_sensor')
router.register(r'fuel-data', FuelDataViewSet, basename='fuel_data')
router.register(r'alerts', AlertViewSet, basename='alert')
router.register(r'geofences', GeofenceViewSet, basename='geofence')
router.register(r'fuel-history', FuelHistoryViewSet, basename='fuel_history')

# URLs del proyecto
urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas por el router
]