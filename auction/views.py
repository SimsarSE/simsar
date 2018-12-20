from django.shortcuts import render, redirect, get_object_or_404
from auction.models import Auction, AuctionReady
from .forms import AuctionForm, AuctionReadyForm


def auction_list(request):
    auctions = Auction.objects.all()
    for auction in auctions:
        Auction.create_auctionReady(auction)
    return render(request, 'auction/auction_list.html', {'auctions': auctions})


def auction_new(request):
    current_user = request.user
    if current_user:
        if request.method == "POST":
            form = AuctionForm(request.POST, request.FILES)
            if form.is_valid():
                auction = form.save(commit=False)
                auction.auctioneer = current_user
                auction.save()
                return redirect('auction_detail', pk=auction.pk)
        else:
            form = AuctionForm()
        return render(request, 'auction/auction_edit.html', {'form': form})
    else:
        return render(request, 'product/product_list.html')


def auction_detail(request, pk):
    auctionReadies = AuctionReady.objects.all().order_by('-auction_price')
    current_user = request.user
    auction = get_object_or_404(Auction, pk=pk)
    if current_user.is_authenticated:
        if auction.is_active:
            form = AuctionReadyForm(request.POST)
            if form.is_valid():
                auctionReady = form.save(commit=False)
                auctionReady.user_ref = current_user
                auctionReady.auction_ref = auction
                return redirect('auction_detail', pk=auction.pk)
            else:
                form = AuctionReadyForm()
            return render(request, 'auction/auctioning.html', {'form':form, 'auction':auction, 'auctionReadies': auctionReadies})
        else:
            return render(request, 'auction/auction_detail.html', {'auction': auction})
    else:
        return redirect('signup')


def auction_edit(request, pk):
    current_user = request.user
    auction = get_object_or_404(Auction, pk=pk)
    if current_user == auction.auctioneer:
        if request.method == "POST":
            form = AuctionForm(request.POST, request.FILES, instance=auction)
            if form.is_valid():
                auction = form.save(commit=False)
                auction.auctioneer = current_user
                auction.save()
                return redirect('auction_detail', pk=auction.pk)
        else:
            form = AuctionForm(instance=auction)
        return render(request, 'auction/auction_edit.html', {'form': form})
    else:
        return render(request, 'auction/auction_list.html')
