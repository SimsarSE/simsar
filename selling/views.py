from django.shortcuts import render, get_object_or_404
from .models import Offers
from product.models import Product

def deal(request, pk):
    print(request.body)