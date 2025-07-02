from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from .models import Product, ProductSerializer

class ProductViewSet(ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

