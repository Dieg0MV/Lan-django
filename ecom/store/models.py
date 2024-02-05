from django.db import models

# Create your models here.

class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.TextField()
    
    def __str__(self):
        return self.productname
    