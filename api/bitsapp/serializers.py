from django.db.models import fields
from rest_framework import serializers
from .models import CustomerModel
from bitsapp import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields ='__all__'