from django.db import models
from django.contrib.auth import get_user_model




# Create your models here.
User=get_user_model()
# public names="";

class Cart(models.Model):
    
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    vendor_id=models.IntegerField()
    product_id=models.IntegerField(null=False)
    name=models.TextField()
    price=models.TextField()
    category=models.CharField(max_length=200)
    rating=models.IntegerField(blank=True,null=True)
    image=models.FileField(max_length=250)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"<Cart {self.name}"
    
   