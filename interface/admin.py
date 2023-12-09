from django.contrib import admin
from .models import Product, Blog, User

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Blog, BlogAdmin)
