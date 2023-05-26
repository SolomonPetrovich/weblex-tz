from .models import *
from rest_framework import serializers
from geopy.distance import geodesic as GD


class CarSerializer(serializers.ModelSerializer):
    number = serializers.CharField(read_only=True)
    current_location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = Car
        fields = ['number', 'current_location', 'capacity']


class ProductSerializer(serializers.ModelSerializer):
    location_pickup = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    location_delivery = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    weight = serializers.IntegerField()
    description = serializers.CharField()
    nearby_cars = serializers.SerializerMethodField()

    def get_nearby_cars(self, obj) -> int:
        cars = Car.objects.all()
        cars_list = []
        for car in cars:
            if GD((obj.location_pickup.latitude, obj.location_pickup.longitude), (car.current_location.latitude, car.current_location.longitude)).miles < 450:
                cars_list.append(car)
        return len(cars_list)

    class Meta:
        model = Product
        fields = ['location_pickup', 'location_delivery', 'weight', 'description', 'nearby_cars']


class ProductUpdateSerializer(serializers.HyperlinkedModelSerializer):
    location_pickup = serializers.CharField(read_only=True)
    location_delivery = serializers.CharField(read_only=True)
    weight = serializers.IntegerField()
    description = serializers.CharField()
    nearby_car_numbers = serializers.SerializerMethodField()

    def get_nearby_car_numbers(self, obj) -> list:
        cars = Car.objects.all()
        cars_list = []
        for car in cars:
            distance = GD((obj.location_pickup.latitude, obj.location_pickup.longitude), (car.current_location.latitude, car.current_location.longitude)).miles
            cars_list.append({'distance': distance, 'car_number': car.number})
        return cars_list
    
    class Meta:
        model = Product
        fields = ['location_pickup', 'location_delivery', 'weight', 'description', 'nearby_car_numbers']