from django.db import models
from products.models import Products

# Create your models here.
class Ratings(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    rating=models.IntegerField(blank=True,null=True)
    rating_text=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"<Ratings {self.product}"
    
