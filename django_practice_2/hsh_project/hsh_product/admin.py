from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAmdin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Product, ProductAmdin)