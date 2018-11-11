from django.db import models

import users
# Create your models here.
class Product(models.Model):
    userid = users.models.id
    productname = models.CharField(max_length=120, verbose_name='Ürün Adı')
    quantity = models.IntegerField(verbose_name='Ürün Miktarı')
    location = models.CharField(max_length=200)
    ekin_tarihi = models.DateField(verbose_name='Ekin Tarihi')
    hasat_tarihi = models.DateField(verbose_name='Hasat Tarihi')
    product_content = models.TextField(verbose_name='ürün Açıklaması')
    publising_date = models.DateTimeField(verbose_name='Yayınlanma Tarihi')
    product_photo = models.