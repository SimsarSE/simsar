from datetime import timedelta

from background_task import background
from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField
from users.models import CustomUser
import time


class Auction(models.Model):
    productname = models.CharField(max_length=120, verbose_name='Product Name')
    quantity = models.IntegerField(verbose_name='Product Quantity')
    location = models.CharField(max_length=200)
    bread_date = models.DateField(verbose_name='Bread Date')
    harvest_date = models.DateField(verbose_name='Harvest Date')
    product_content = models.TextField(verbose_name='Product Information')
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='TRY')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Create Date')
    product_photo = models.ImageField(verbose_name='Product Photo', blank=True)
    auctioneer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='auctioneer', default=0)
    min_auction_time = models.IntegerField(verbose_name='Auction period of validity')
    start_time = models.DateTimeField(verbose_name='Start Time')
    is_active = models.BooleanField(default=False)
    is_end = models.BooleanField(default=False)

    def group_name(self):
        return "auction-%s" % self.id

    def create_auctionReady(self):
        isNow = self.start_time.timestamp() - timezone.now().timestamp()
        if (isNow <= 0):
            self.is_active = True
            self.save()

    def countdown(self):
        minTime = self.start_time + timedelta(minutes=self.min_auction_time)
        time = minTime - timezone.now()
        if minTime > timezone.now():
            return time.seconds
        return -1

    def end_of_auction(self):
        try:
            last_time = AuctionReady.objects.filter(auction_ref=self).order_by(
                "-time_stamp").first().time_stamp + timedelta(seconds=60)
            now = timezone.now()
            if last_time < now:
                self.is_end = True
                self.save()
        except:
            ownerness = self.start_time + timedelta(minutes=self.min_auction_time) + timedelta(seconds=60)
            now = timezone.now()
            if ownerness < now:
                self.is_end = True
                self.save()


class AuctionReady(models.Model):
    auction_ref = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user_ref = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    auction_price = MoneyField(max_digits=14, decimal_places=2, default_currency='TRY', default=0)
    time_stamp = models.DateTimeField(default=timezone.now, verbose_name='Time')

    #
