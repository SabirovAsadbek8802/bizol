from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact),
    path('login-register/', views.login_register),
    path('reset-password/', views.account_dashboard),
    path('edit-address/', views.account_edit_address),
    path('edit/', views.account_edit),
    path('orders/', views.account_orders),
    path('wishlist/', views.account_wishlist),
]
