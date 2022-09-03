from .models import Cart
from rest_framework import serializers
from authentication.models import User

class CartCreationSerializer(serializers.ModelSerializer):
    customer=User()
    vendor_id=serializers.IntegerField(allow_null=False)
    product_id=serializers.IntegerField(allow_null=False)
    quantity=serializers.IntegerField(default=1)
    name=serializers.CharField()
    price=serializers.IntegerField()
    category=serializers.CharField(max_length=200)
    rating=serializers.IntegerField(allow_null=True)
    image=serializers.ImageField(allow_null=True)

    class Meta:
        model=Cart
        fields=['id','customer','vendor_id','product_id','name','quantity','price','category','rating','image']

class ProductQuantityUpdateSerializer(serializers.ModelSerializer):
    quantity=serializers.IntegerField(default=1)


    class Meta:
        model=Cart
        fields=['quantity']