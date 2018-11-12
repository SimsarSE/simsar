from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Product(models.Model):
    productname = models.CharField(max_length=120, verbose_name='Product Name')
    quantity = models.IntegerField(verbose_name='Product Quantity')
    location = models.CharField(max_length=200)
    bread_date = models.DateField(verbose_name='Bread Date')
    harvest_date = models.DateField(verbose_name='Harvest Date')
    product_content = models.TextField(verbose_name='Product Information')
    create_date = models.DateTimeField(default=timezone.now,verbose_name='Create Date')
    product_photo = models.ImageField(verbose_name='Product Photo',blank=True)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='seller', default=0)