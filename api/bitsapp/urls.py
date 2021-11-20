from django.urls import path
from . import views

urlpatterns = [
    # ==================================================
    # ============ BACKEND API's URLS ==================
    # path('api/customerAPI/', views.customerAPI, name="customerAPI"),

    # ===================================================
    # ============ FRONTEND URLS ========================
    path('', views.index, name="index"),
    path('dashboard/dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/employee/', views.employee, name='employee'),
    path("dashboard/product/", views.product, name='product'),
    path('dashboard/customer/', views.customer, name="customer"),
]
