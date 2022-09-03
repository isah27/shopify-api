from itertools import product
from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()
# Create your models here.
class Order(models.Model):
    ORDER_STATUS=(
        ('PENDING','PENDING'),
        ('IN_TRANSIT','IN TRANSIT'),
        ('DELIVERED', 'DELIVERED'),
    )
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    vendor_id=models.IntegerField()
    product_id=models.IntegerField()
    product_name=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    order_status=models.CharField(max_length=20,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"<Order {self.order_status} by {self.customer.id}>"