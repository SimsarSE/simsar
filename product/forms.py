from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
        'productname', 'quantity', 'location', 'bread_date', 'harvest_date', 'product_content', 'price', 'product_photo')
        widgets={
            'bread_date': DatePickerInput(format='%d-%m-%Y'),
            'harvest_date': DatePickerInput(format='%d-%m-%Y'),
        }
