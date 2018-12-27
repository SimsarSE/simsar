from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from djmoney.models.fields import MoneyField

from .models import Auction, AuctionReady


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = (
        'productname', 'quantity', 'location', 'bread_date', 'harvest_date', 'product_content', 'price', 'product_photo', 'min_auction_time', 'start_time')
        widgets = {
            'bread_date': DatePickerInput(format='%d-%m-%Y'),
            'harvest_date': DatePickerInput(format='%d-%m-%Y'),
            'start_time': DateTimePickerInput(format='%d-%m-%Y %H-%M'),
        }

class AuctionReadyForm(forms.ModelForm):
    class Meta:
        model = AuctionReady
        fields = (
            'auction_price',
        )
