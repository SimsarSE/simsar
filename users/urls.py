from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', views.home, name='home'),
    path('profile/', views.view_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('password/', views.change_password, name='change_password')

]