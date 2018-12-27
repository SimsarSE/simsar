from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.deal, name='deal'),
    path('buy/<int:pk>', views.buy, name='buy'),
    path('accept_offer/<int:pk>', views.accept, name='accept_offer'),
    path('reject_offer/<int:pk>', views.reject, name='reject_offer'),
]