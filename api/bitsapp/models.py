from django.db import models

# Customers DB Table
class CustomerModel(models.Model):
    # admin_id = models.CharField(max_length=10)
    fullname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    District = models.CharField(max_length=80)
    Address = models.CharField(max_length=122)
    month_year = models.CharField(max_length=122)
    class Meta:
        db_table = 'customer_tb'

# Employees DB Table
class EmployeeModel(models.Model):
    admin_id = models.CharField(max_length=10)
    fullname = models.CharField(max_length=122)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=122)
    data_of_birth = models.CharField(max_length=90)
    degree = models.CharField(max_length=122)
    position = models.CharField(max_length=122)
    salary = models.CharField(max_length=90)
    InD = models.CharField(max_length=90)
    bank_account_number = models.CharField(max_length=90)
    bank_name = models.CharField(max_length=90)
    martual_status = models.CharField(max_length=90)
    gender = models.CharField(max_length=80)
    birth_place = models.CharField(max_length=90)
    nationality = models.CharField(max_length=90)
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=90)
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    class Meta:
        db_table = 'employee_tb'

# Category DB Table
class CategoryModel(models.Model):
    admin_id = models.CharField(max_length=11)
    category_name = models.CharField(max_length=122)
    class Meta:
        db_table = 'category_tb' 

# Product DB Table
class ProductModel(models.Model):
    admin_id = models.CharField(max_length=11)
    category_id = models.CharField(max_length=11)
    product_name = models.CharField(max_length=122)
    unity_price = models.CharField(max_length=60)
    quantity = models.CharField(max_length=60)
    status = models.CharField(max_length=21)
    desciption = models.TextField(max_length=500)
    month_year = models.CharField(max_length=122)
    class Meta:
        db_table = 'product_tb' 

# Invoice DB Table
class InvoiceModel(models.Model):
    admin_id = models.BigIntegerField()
    customer_id = models.BigIntegerField()
    dueDate = models.CharField(max_length=60)
    discount = models.SmallIntegerField()
    vat = models.SmallIntegerField()
    status = models.CharField(max_length=50)
    month_year = models.CharField(max_length=122)
    class Meta:
        db_table = 'invoice_tb' 

# InvoiceContainer DB Table
class InvoiceContainerModel(models.Model):
    admin_id = models.BigIntegerField()
    invoice_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    qty = models.SmallIntegerField()
    month_year = models.CharField(max_length=122)
    class Meta:
        db_table = 'invoice_container_tb' 
