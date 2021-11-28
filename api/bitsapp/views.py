from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer
import requests

from .models import CustomerModel, ProductModel

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
    employeeshow = requests.get('http://127.0.0.1:8000/api/employee/?format=json')
    results = employeeshow.json()
    return render(request, 'dashboard/employee.html', {'EmployeeModel':results})

# Product Page
def product(request):
    productshow = requests.get('http://127.0.0.1:8000/api/product/?format=json')
    results = productshow.json()
    return render(request, 'dashboard/product.html', {'ProductModel':results})

# Product View Page
def product_detail(request, pk):
    product_detailshow = ProductModel.get(id=pk)
    context = {
        'productdetail' : product_detailshow
    }
    return render(request, 'dashboard/product_detail.html', context)

# Customer Page
def customer(request):
    customershow = requests.get('http://127.0.0.1:8000/api/customer/?format=json')
    results = customershow.json()

    return render(request,'dashboard/customer.html', {'CustomerModel':results})

# # Category Page
def category(request):
    categoryshow = requests.get('http://127.0.0.1:8000/api/category/?format=json')
    results = categoryshow.json()
    return render(request, 'dashboard/product.html', {'CategoryModel':results})