from rest_framework  import serializers
from .models import Order
from authentication.models import User

class OrderCreationSerializer(serializers.ModelSerializer):
    customer=User()
    product_id=serializers.IntegerField()
    vendor_id=serializers.IntegerField()
    product_name=serializers.CharField()
    price=serializers.IntegerField()
    quantity=serializers.IntegerField()
    order_status=serializers.CharField(default='PENDING')
    
    class Meta:
        model=Order
        fields=['id','customer','vendor_id','product_id','product_name','price','quantity','order_status']
        
class OrderDetailSerializer(serializers.ModelSerializer):
    customer=User()
    product_id=serializers.IntegerField()
    product_name=serializers.CharField()
    price=serializers.IntegerField()
    quantity=serializers.IntegerField(default=1)
    order_status=serializers.CharField(default='PENDING')
    vendor_id=serializers.IntegerField()
    
    
    class Meta:
        model=Order
        fields=['id','customer','product_id','product_name','price','quantity','order_status','vendor_id','created_at','updated_at']
   
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status=serializers.CharField(default='PENDING')


    class Meta:
        model=Order
        fields=['order_status']