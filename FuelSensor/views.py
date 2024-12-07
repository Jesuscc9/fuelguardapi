from rest_framework import viewsets
from .models import Truck, FuelSensor, FuelData, Alert, Geofence, FuelHistory
from .serializers import (
    TruckReadSerializer,
    TruckWriteSerializer,
    FuelSensorReadSerializer,
    FuelSensorWriteSerializer,
    FuelDataReadSerializer,
    FuelDataWriteSerializer,
    AlertReadSerializer,
    AlertWriteSerializer,
    GeofenceReadSerializer,
    GeofenceWriteSerializer,
    FuelHistoryReadSerializer,
    FuelHistoryWriteSerializer,
)
from rest_framework.permissions import IsAuthenticated


# ====== ViewSet para Truck ======
class TruckViewSet(viewsets.ModelViewSet):
    queryset = Truck.objects.all()

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TruckReadSerializer
        return TruckWriteSerializer


# ====== ViewSet para FuelSensor ======
class FuelSensorViewSet(viewsets.ModelViewSet):
    queryset = FuelSensor.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FuelSensorReadSerializer
        return FuelSensorWriteSerializer


# ====== ViewSet para FuelData ======
class FuelDataViewSet(viewsets.ModelViewSet):
    queryset = FuelData.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FuelDataReadSerializer
        return FuelDataWriteSerializer


# ====== ViewSet para Alert ======
class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return AlertReadSerializer
        return AlertWriteSerializer


# ====== ViewSet para Geofence ======
class GeofenceViewSet(viewsets.ModelViewSet):
    queryset = Geofence.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return GeofenceReadSerializer
        return GeofenceWriteSerializer


# ====== ViewSet para FuelHistory ======
class FuelHistoryViewSet(viewsets.ModelViewSet):
    queryset = FuelHistory.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FuelHistoryReadSerializer
        return FuelHistoryWriteSerializer
