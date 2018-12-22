from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, EditProfileForm
from users.models import CustomUser
from product.models import Product

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    template_name = 'signup.html'

def view_profile(request, pk):
    profile = get_object_or_404(CustomUser, pk=pk)
    products = Product.objects.all()
    args = {'user': profile, 'products': products}
    return render(request, 'profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}

    return render(request, 'change_password.html', args)

def product_info(request):
    products = Product.objects.all()

    return render(request, 'profile.html' , {'products': products} )