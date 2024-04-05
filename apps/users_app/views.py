from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def login_register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['login_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are successfully logged in!"))
            return redirect('home')
        else:
            messages.success(request, ("Something went wrong! Please try again!"))
            return redirect('login')
    else:
        return render(request, 'login_register.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have successfully logged out! "))
    return redirect('login')

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
