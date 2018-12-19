from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

from users.models import CustomUser


class SoldProduct(models.Model):
    sold_cost = models.IntegerField(verbose_name='sold_cost')
    sold_date = models.DateTimeField(default=timezone.now, verbose_name='sold_date')
    sold_seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sold_seller', default=0)
    sold_buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sold_buyer', default=0)

class Offers(models.Model):
    offer_cost = models.IntegerField(verbose_name='offer_cost')
    offer_date = models.DateTimeField(default=timezone.now, verbose_name='offer_date')
    offer_seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='offer_seller', default=0)
    offer_bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='offer_bidder', default=0)