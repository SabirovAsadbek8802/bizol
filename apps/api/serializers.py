from rest_framework.serializers import ModelSerializer
from apps.store_app.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'