from django.db import models
from django.utils.timezone import now
from .choices import ProductStatusChoices
from apps.users_app.models import Customer
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/products')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    slug = models.SlugField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places = 2, default=0)
    address = models.CharField(max_length = 255, blank=False, null=False)
    phone_number = models.CharField(max_length=30, blank=False, null=False)
    date = models.DateTimeField()
    status = models.SmallIntegerField(choices = ProductStatusChoices.choices, null=False)
    