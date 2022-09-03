from dataclasses import fields
from rest_framework import serializers
from .models import Ratings
from products.models import Products

class RatingCreationSerializer(serializers.ModelSerializer):
    product=Products()
    rating=serializers.IntegerField()
    rating_text=serializers.CharField()
    
    class Meta:
        model=Ratings
        fields=['product','rating','rating_text']
    
class ProductRatingUpdateSerializer(serializers.ModelSerializer):
    rating=serializers.IntegerField()
    rating_text=serializers.CharField()


    class Meta:
        model=Ratings
        fields=['rating','rating_text','updated_at']