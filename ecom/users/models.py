from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.TextField()
    password = models.CharField(max_length=3000)    
    email = models.EmailField(max_length=250)
