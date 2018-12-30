from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from template_forms import bs4

class CustomUserCreationForm(bs4.BlockForm, UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser

        fields = ('first_name', 'last_name', 'username', 'email', 'GSM',)
        widgets = {
            'GSM': forms.TextInput(attrs={'placeholder': '+90 xxx xxx xx xx'})
        }

class EditProfileForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'username',
            'GSM',
            'password'
)