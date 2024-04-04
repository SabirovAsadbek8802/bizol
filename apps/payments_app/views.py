from django.shortcuts import render


def cart(request):
    return render(request, 'shop_cart.html')

def checkout(request):
    return render(request, 'shop_checkout.html')

def order_complete(request):
    return render(request, 'shop_order_complete.html')

def order_tracking(request):
    return render(request, 'shop_order_tracking.html')

def shop(request):
    return render(request, 'shop.html')