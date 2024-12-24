from django.db import models

class Drone(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    status = models.CharField(max_length=50, default="active")
    
    class Meta:
        db_table = "drones"  # Указываем имя таблицы

    def __str__(self):
        return self.name


class ImageData(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE, related_name="images")
    image_path = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = "images"  # Указываем имя таблицы

    def __str__(self):
        return f"Image for Drone {self.drone.name} at {self.timestamp}"
