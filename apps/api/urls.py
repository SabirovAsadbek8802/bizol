from django.urls import path
from .views import ProductAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductAPIView, basename='product')

urlpatterns = router.urls

