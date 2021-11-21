from django.db.models import fields
from rest_framework import serializers
from .models import CustomerModel, CategoryModel, EmployeeModel, ProductModel, InvoiceModel, InvoiceContainerModel
from bitsapp import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields ='__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields ='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields ='__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceModel
        fields ='__all__'

class InvoiceContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceContainerModel
        fields ='__all__'