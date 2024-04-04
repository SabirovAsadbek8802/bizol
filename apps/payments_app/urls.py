from django.urls import path
from . import views


urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='shop-checkout'),
    path('order/complete/', views.order_complete, name='order-complete'),
    path('', views.shop, name='shop'),
]
