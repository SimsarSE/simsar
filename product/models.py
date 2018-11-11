from django.db import models

import users
# Create your models here.
class Product(models.Model):
    userid = users.models.id
    productname = models.CharField(max_length=120, verbose_name='ürün adı')
    quantity = models.IntegerField(verbose_name='miktar')
    location = models.CharField(max_length=200)