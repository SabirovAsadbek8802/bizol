from django.shortcuts import render

def login_register(request):
    return render(request, 'login_register.html')

def reset_password(request):
    return render(request, 'reset_password.html')

def account_dashboard(request):
    return render(request, 'account_dashboard.html')


def account_edit_address(request):
    return render(request, 'account_edit_address.html')


def account_edit(request):
    return render(request, 'account_edit.html')


def account_orders(request):
    return render(request, 'account_orders.html')

def account_wishlist(request):
    return render(request, 'account_wishlist.html')
