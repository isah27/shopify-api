from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    category=serializers.CharField()
    
    class Meta:
        model=Category
        fields=['id','category']