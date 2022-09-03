from django.contrib import admin
from .models import Products

# Register your models here.
@admin.register(Products)

class OrderAdmin(admin.ModelAdmin):
    list_display=['name','description','price','created_at']
    # list_filter=['created_at']