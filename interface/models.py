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
    discount_price = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True)

class Blog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    title1 = models.CharField(max_length=200, null=True, blank=True)
    title2 = models.CharField(max_length=200, null=True, blank=True)
    title3 = models.CharField(max_length=200, null=True, blank=True)
    creator = models.CharField(max_length=50)
    content = models.TextField()
    content1 = models.TextField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, upload_to="images/")
    image_1 = models.ImageField(null=True, upload_to="images/", blank=True)
    image_2 = models.ImageField(null=True, upload_to="images/", blank=True)
    image_3 = models.ImageField(null=True, upload_to="images/", blank=True)
    modified_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=500,null=True, blank=True)

    
    
