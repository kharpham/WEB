# Generated by Django 4.2.4 on 2024-01-05 03:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interface', '0012_alter_product_likes_alter_product_shoppers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='shoppers',
            field=models.ManyToManyField(blank=True, null=True, related_name='shopping_cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
