from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.deal, name='deal'),
    path('buy/<int:pk>', views.deal, name='buy'),
]