from rest_framework import generics, status
from rest_framework.permissions import *
from rest_framework.views import Response

from .models import *
from .serializers import *


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        weight = self.request.query_params.get('weight')
        if weight == None:
            queryset = Product.objects.all()
        else:
            queryset = Product.objects.filter(weight=weight)
        
        return queryset


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductUpdateSerializer
    queryset = Product.objects.all()


class CarUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
