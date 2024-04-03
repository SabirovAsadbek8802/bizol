from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.blogList, name='blog-list'),
    path('<int:pk>/', views.blogSingle, name='blog-detail'),
]

