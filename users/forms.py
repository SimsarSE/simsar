from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from template_forms import bs4

class CustomUserCreationForm(bs4.BlockForm, UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser

        fields = ('first_name', 'last_name', 'username', 'email', 'GSM',)

class CustomUserChangeForm(bs4.BlockForm, UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'GSM', )