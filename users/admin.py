from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, EditProfileForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = EditProfileForm
    model = CustomUser
    list_display = ['email', 'username', 'GSM']

admin.site.register(CustomUser, CustomUserAdmin)
