from django.db import models


class CustomerModel(models.Model):
    admin_id = models.CharField(max_length=10)
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