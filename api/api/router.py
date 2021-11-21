from bitsapp.viewsets import CustomerViewset, CategoryViewset, EmployeeViewset, ProductViewset, InvoiceViewset, InvoiceContainerViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', CustomerViewset)
router.register('employee',EmployeeViewset)
router.register('category',CategoryViewset)
router.register('product', ProductViewset)
router.register('invoice', InvoiceViewset)
router.register('invoicecontainer', InvoiceContainerViewset)