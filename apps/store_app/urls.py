from django.urls import path
from . import views


urlpatterns = [
    path('lookbook/', views.lookbook, name='lookbook'),
    path('product/simple/', views.product_simple, name='product-simple'),
    path('product/onsale/', views.product_onsale),
    path('product/out-of-stock/', views.product_outofstock),
    path('location/', views.store_location),
]
