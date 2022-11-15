from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    c_email = models.CharField(max_length=100)
    c_phone = models.BigIntegerField()
    c_address = models.CharField(max_length=300)
    c_password = models.CharField(max_length=30)

