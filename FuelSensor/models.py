from django.db import models

# Modelo para los camiones
class Truck(models.Model):
    identifier = models.CharField(max_length=50, unique=True)  # Identificador único del camión
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.identifier} ({self.model})"

# Modelo para los sensores de combustible
class FuelSensor(models.Model):
    truck = models.OneToOneField(Truck, on_delete=models.CASCADE, related_name='fuel_sensor')
    sensor_type = models.CharField(max_length=50, choices=[('pressure', 'Pressure'), ('level', 'Level')])
    certification = models.CharField(max_length=50, choices=[('atex', 'ATEX'), ('iecex', 'IECEx')])

    def __str__(self):
        return f"Sensor {self.sensor_type} for Truck {self.truck.identifier}"

# Modelo para datos de monitoreo de combustible
class FuelData(models.Model):
    sensor = models.ForeignKey(FuelSensor, on_delete=models.CASCADE, related_name='fuel_data')
    timestamp = models.DateTimeField(auto_now_add=True)
    fuel_level = models.FloatField()  # Nivel de combustible en litros o porcentaje
    location = models.CharField(max_length=255)  # Ubicación GPS

    def __str__(self):
        return f"Data from {self.sensor} at {self.timestamp}"

# Modelo para alertas
class Alert(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='alerts')
    alert_type = models.CharField(max_length=100, choices=[
        ('low_Fuel', 'Low Fuel'),
        ('fuel_theft', 'Fuel Theft'),
        ('geofence_breach', 'Geofence Breach')
    ])
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Alert: {self.alert_type} for {self.truck.identifier}"

# Modelo para geovallas
class Geofence(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='geofences')
    name = models.CharField(max_length=100)
    coordinates = models.TextField()  # Podría ser un JSON o lista de coordenadas GPS

    def __str__(self):
        return f"Geofence {self.name} for Truck {self.truck.identifier}"

# Modelo para historial
class FuelHistory(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='fuel_history')
    date = models.DateField()
    total_fuel_used = models.FloatField()
    total_distance_traveled = models.FloatField()

    def __str__(self):
        return f"History for {self.truck.identifier} on {self.date}"