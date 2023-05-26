from .models import Car, Location
import random


def change_location_of_car():
    car_list = Car.objects.all()

    for car in car_list:
        car.location = random.choice(Location.objects.all())
        car.save()