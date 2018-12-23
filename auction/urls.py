from django.urls import path
from . import views

urlpatterns = [
    path('list', views.auction_list, name='auction_list'),
    path('new', views.auction_new, name='auction_new'),
    path('<int:pk>', views.auction_detail, name='auction_detail'),
    path('<int:pk>/edit', views.auction_edit, name='auction_edit'),
    path('last_auction/<int:pk>', views.last_auction_ready, name='last_auction'),
    path('extra_time/<int:pk>', views.extra_time, name='extra_time'),
    path('sold_auction/<int:pk>', views.sold_action, name='sold_auction'),
]