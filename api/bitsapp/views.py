from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer
import requests

from .models import CustomerModel

# =====================================================
# ======== BACKEND - DATABASE API's ===================
# =====================================================
@api_view(['GET'])
def customerAPI(request):
    if request.method=='GET':
        results = CustomerModel.objects.all()
        serialize = CustomerSerializer(results, many=True)
        return Response(serialize.data)





# ============================================
# ====== FRONTEND - DESIGN TEMPLATE ==========
# ============================================

# HomePage
def index(request):
    return render(request,'index.html', {})

# Dashboard Page
def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {})

# Employee Page
def employee(request):
    return render(request, 'dashboard/employee.html', {})

# Product Page
def product(request):
    return render(request, 'dashboard/product.html', {})

# Customer Page
def customer(request):
    customershow = requests.get('http://127.0.0.1:8000/api/customer/')
    results = customershow.json()

    return render(request,'dashboard/customer.html', {'CustomerModel':results})
