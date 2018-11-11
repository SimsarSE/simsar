from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
        'productname', 'quantity', 'location', 'bread_date', 'harvest_date', 'product_content','product_photo')

