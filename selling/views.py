from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Offers
from product.models import Product

def deal(request, pk):
    buyer = request.user
    product = Product.objects.get(id=pk)
    seller = product.seller
    cost = request.POST['offer']
    offers = Offers(offer_cost=cost, offer_product=product, offer_seller=seller, offer_bidder=buyer)
    print(offers.offer_cost)
    offers.save()
    return HttpResponse('')