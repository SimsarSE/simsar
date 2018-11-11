from django.db import models

import users
# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=120, verbose_name='Product Name')
    quantity = models.IntegerField(verbose_name='Product Quantity')
    location = models.CharField(max_length=200)
    bread_date = models.DateField(verbose_name='Bread Date')
    harvest_date = models.DateField(verbose_name='Harvest Date')
    product_content = models.TextField(verbose_name='Product Information')
    publising_date = models.DateTimeField(verbose_name='Publishing Date')
    product_photo = models.ImageField(verbose_name='Product Photo')