from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Offers, SoldProduct
from product.models import Product
from djmoney.money import Money


def deal(request, pk):
    buyer = request.user
    product = Product.objects.get(id=pk)
    seller = product.seller
    cost = request.POST['offer']
    offers = Offers(offer_cost=Money(cost, 'TRY'), offer_product=product, offer_seller=seller, offer_bidder=buyer)
    offers.save()
    return HttpResponse('')

def buy(request, pk):
    buyer = request.user
    product = Product.objects.get(id=pk)
    seller = product.seller
    cost = product.price
    sold = SoldProduct(sold_cost=cost, sold_buyer=buyer, sold_seller=seller, sold_product=product)
    sold.save()
    product.is_sold = True
    product.save()
    return HttpResponse('')
