from .models import Products
from rest_framework import serializers
from authentication.models import User
from category.models import Category


class ProductCreationSerializer(serializers.ModelSerializer):
    vendor=User()
    name=serializers.CharField()
    description=serializers.CharField()
    price=serializers.CharField()
    category=Category()
    image=serializers.FileField(required=False,allow_null=True)

    class Meta:
        model=Products
        fields=['id','vendor','name','description','price','category','image']

class ProductDetailSerializer(serializers.ModelSerializer):
    vendor=User()
    name=serializers.CharField()
    description=serializers.CharField()
    price=serializers.CharField()
    category=Category()
    image=serializers.FileField(required=False,allow_null=True)
    
    class Meta:
        model=Products
        fields=['id','vendor','name','description','price','category',
                'image','created_at','updated_at']
