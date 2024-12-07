from rest_framework import serializers
from .models import Truck, FuelSensor, FuelData, Alert, Geofence, FuelHistory

# ====== Serializers para Truck ======


class TruckReadSerializer(serializers.ModelSerializer):
    fuel_sensor = serializers.StringRelatedField()  # Relación al sensor
    alerts = serializers.StringRelatedField(many=True)  # Relación a alertas
    geofences = serializers.StringRelatedField(many=True)  # Relación a geovallas
    fuel_history = serializers.StringRelatedField(many=True)  # Relación a historial

    class Meta:
        model = Truck
        fields = [
            "id",
            "identifier",
            "model",
            "year",
            "fuel_sensor",
            "alerts",
            "geofences",
            "fuel_history",
        ]


class TruckWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ["id", "identifier", "model", "year"]


# ====== Serializers para FuelSensor ======


class FuelSensorReadSerializer(serializers.ModelSerializer):
    truck = serializers.StringRelatedField()  # Relación al camión

    class Meta:
        model = FuelSensor
        fields = ["id", "truck", "sensor_type", "certification"]


class FuelSensorWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelSensor
        fields = ["id", "truck", "sensor_type", "certification"]


# ====== Serializers para FuelData ======


class FuelDataReadSerializer(serializers.ModelSerializer):
    sensor = serializers.StringRelatedField()  # Relación al sensor

    class Meta:
        model = FuelData
        fields = ["id", "sensor", "timestamp", "fuel_level", "location"]


class FuelDataWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelData
        fields = ["id", "sensor", "fuel_level", "location"]


# ====== Serializers para Alert ======


class AlertReadSerializer(serializers.ModelSerializer):
    truck = serializers.StringRelatedField()  # Relación al camión

    class Meta:
        model = Alert
        fields = ["id", "truck", "alert_type", "message", "timestamp", "resolved"]


class AlertWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ["id", "truck", "alert_type", "message", "resolved"]


# ====== Serializers para Geofence ======


class GeofenceReadSerializer(serializers.ModelSerializer):
    truck = serializers.StringRelatedField()  # Relación al camión

    class Meta:
        model = Geofence
        fields = ["id", "truck", "name", "lat", "lng", "radius"]


class GeofenceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ["id", "truck", "name", "lat", "lng", "radius"]


# ====== Serializers para FuelHistory ======


class FuelHistoryReadSerializer(serializers.ModelSerializer):
    truck = serializers.StringRelatedField()  # Relación al camión

    class Meta:
        model = FuelHistory
        fields = ["id", "truck", "date", "total_fuel_used", "total_distance_traveled"]


class FuelHistoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelHistory
        fields = ["id", "truck", "date", "total_fuel_used", "total_distance_traveled"]
