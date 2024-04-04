from django.db import models
import os
from django.core.exceptions import ValidationError

# def validate_image_extension(value):
#     valid_extensions = ['.ico', '.png', '.jpg']
#     ext = os.path.splitext(value.name)[1]
#     if ext.lower() not in valid_extensions:
#         raise ValidationError('Only ICO, PNG, or JPG files are allowed.')

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='uploads/products/icons/')
    children = models.ForeignKey('self', on_delete = models.DO_NOTHING, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        if self.children:
            return f'{self.name} - {self.children}'
        else:
            return f'{self.name}'
    