from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Location(models.Model):
    zipcode = models.CharField(max_length=500, primary_key=True)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.city


class Product(models.Model):
    location_pickup = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='location_pickup')
    location_delivery = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='location_delivery')
    weight = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(1000),
            MinValueValidator(1)
        ]
    )
    description = models.TextField()

    def __str__(self) -> str:
        return self.description


class Car(models.Model):
    number = models.CharField(max_length=500, unique=True)
    current_location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='current_location')
    capacity = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(1000),
            MinValueValidator(1)
        ]
    )

    def __str__(self) -> str:
        return self.number