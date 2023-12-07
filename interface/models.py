from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    category = models.CharField(max_length=64)
    subcategory = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    discount_price = models.DecimalField(max_digits=9, decimal_places=0)

class Blog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    creator = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(null=True, upload_to="images/")
    image_1 = models.ImageField(null=True, upload_to="images/")
    image_2 = models.ImageField(null=True, upload_to="images/")
    image_3 = models.ImageField(null=True, upload_to="images/")
    modified_timestamp = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500)

    
    
