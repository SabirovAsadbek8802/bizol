from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .choices import ProductStatusChoices

# def validate_image_extension(value):
#     valid_extensions = ['.ico', '.png', '.jpg']
#     ext = os.path.splitext(value.name)[1]
#     if ext.lower() not in valid_extensions:
#         raise ValidationError('Only ICO, PNG, or JPG files are allowed.')

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='uploads/icons/')
    children = models.ForeignKey('self', on_delete = models.DO_NOTHING, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        if self.children:
            return f'{self.name} - {self.children}'
        else:
            return f'{self.name}'
    
    
class Order(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    product = models.ForeignKey('store_app.Product', on_delete=models.CASCADE, related_name = 'orders')
    quantity = models.DecimalField(default=0, max_digits = 4, decimal_places = 2, blank=False, null=False)
    status = models.SmallIntegerField(choices = ProductStatusChoices.choices, null=False)
    date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=30, blank=False, null=False)
    
    def __str__(self):
        return f'{self.username} - {self.delivery_address}' 
    
    

    
    