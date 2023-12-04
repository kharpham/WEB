from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=64)
    subcategory = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()

class Blog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    creator = models.CharField(max_length=50)
    content = models.TextField()

    
    
