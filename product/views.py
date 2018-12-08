from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


def product_new(request):
    current_user = request.user
    if current_user:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.seller = current_user
                product.save()
                return redirect('product_detail', pk=product.pk)
        else:
            form = ProductForm()
        return render(request, 'product/product_edit.html', {'form': form})
    else:
        return render(request, 'product/product_list.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})


def product_edit(request, pk):
    current_user = request.user
    product = get_object_or_404(Product, pk=pk)
    if current_user == product.seller:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                product = form.save(commit=False)
                product.seller = current_user
                product.save()
                return redirect('product_detail', pk=product.pk)
        else:
            form = ProductForm(instance=product)
        return render(request, 'product/product_edit.html', {'form': form})
    else:
        return render(request, 'product/product_list.html')
