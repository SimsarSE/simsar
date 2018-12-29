from django import forms

from .models import Auction, AuctionReady


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = (
        'productname', 'quantity', 'location', 'bread_date', 'harvest_date', 'product_content', 'price', 'product_photo', 'min_auction_time', 'start_time')
        widgets = {
            'bread_date': forms.DateInput(attrs={'type': 'date'}),
            'harvest_date': forms.DateInput(attrs={'type': 'date'}),
        }
class AuctionReadyForm(forms.ModelForm):
    class Meta:
        model = AuctionReady
        fields = (
            'auction_price',
        )
