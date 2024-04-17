from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login_register, name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('reset-password/', views.reset_password),
    path('edit-address/', views.account_edit_address),
    path('edit/', views.account_edit),
    path('orders/', views.account_orders),
    path('wishlist/', views.account_wishlist),
    path('profile/', views.account_dashboard, name='account-profile'),
]
