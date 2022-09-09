from django.db import models
from django.contrib.auth import get_user_model
from authentication.models import User
from category.models import Category


# Create your models here.
User=get_user_model()


class Products(models.Model):
    vendor=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    description=models.TextField()
    price=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"<Products {self.name}"
    
   
