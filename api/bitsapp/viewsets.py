from rest_framework import viewsets
from . import models
from . import serializers

# Customer View Set
class CustomerViewset(viewsets.ModelViewSet):
    queryset = models.CustomerModel.objects.all()
    serializer_class = serializers.CustomerSerializer

# Employee View Set
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.EmployeeModel.objects.all()
    serializer_class = serializers.EmployeeSerializer

# Category View Set
class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer

# Product View Set
class ProductViewset(viewsets.ModelViewSet):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

# Invoice View Set
class InvoiceViewset(viewsets.ModelViewSet):
    queryset = models.InvoiceModel.objects.all()
    serializer_class = serializers.InvoiceSerializer

# Invoice Container View Set
class InvoiceContainerViewset(viewsets.ModelViewSet):
    queryset = models.InvoiceContainerModel.objects.all()
    serializer_class = serializers.InvoiceContainerSerializer