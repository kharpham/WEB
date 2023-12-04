# Generated by Django 4.2.4 on 2023-12-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('category', models.CharField(max_length=64)),
                ('subcategory', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]