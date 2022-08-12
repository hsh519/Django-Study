from csv import list_dialects
from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

admin.site.register(Order, OrderAdmin)
