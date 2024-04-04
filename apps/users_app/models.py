from django.db import models
from django.core.validators import RegexValidator

    
class Customer(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15,
                                    validators=[
                                        RegexValidator(
                                            regex=r'^\+?1?\d{9,15}$',
                                            message="Phone number must be entered in the format: '+99899...'. Up to 15 digits allowed."
                                        )
                                    ], null=True)
    password = models.CharField(max_length = 255)
    
    def __str__(self):
        return f'{self.first_name} - {self.last_name}'