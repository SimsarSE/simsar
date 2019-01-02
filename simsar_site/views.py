from django.shortcuts import redirect


def home_page(request):
    print("asd")
    return redirect('product_list')