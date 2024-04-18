from django.db import models
from django.utils.timezone import now
from ..main_app.choices import ProductStatusChoices
from apps.users_app.models import Customer
from django.utils.text import slugify
from apps.main_app.models import Category
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/products')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
