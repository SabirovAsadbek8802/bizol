from django.shortcuts import render


def lookbook(request):
    return render(request, 'lookbook.html')

def product_simple(request):
    return render(request, 'product1_simple.html')

def product_onsale(request):
    return render(request, 'product5_onsale.html')

def product_outofstock(request):
    return render(request, 'product6_outofstock.html')

def store_location(request):
    return render(request, 'store_location.html')