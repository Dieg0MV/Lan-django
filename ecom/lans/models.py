from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class landis(models.Model):
    Title = models.CharField(max_length=100)
    Info = models.TextField(blank=True)
    datacreate = models.DateTimeField(auto_now_add=True)
    img = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    