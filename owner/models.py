from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=30,default='')
    photo = models.ImageField(upload_to='owner/',default='')

class house(models.Model):
    



