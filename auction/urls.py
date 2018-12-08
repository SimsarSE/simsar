from django.urls import path
from . import views

urlpatterns = [
    path('list', views.auction_list, name='auction_list'),
    path('new', views.auction_new, name='auction_new'),
    path('<int:pk>', views.auction_detail, name='auction_detail'),
    path('<int:pk>/edit', views.auction_edit, name='auction_edit'),
]