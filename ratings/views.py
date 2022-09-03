from django.shortcuts import render
from rest_framework import generics,status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from . import serializers
from .models import Ratings

# Create your views here.
class RatinCreationView(generics.GenericAPIView):
    serializer_class=serializers.RatingCreationSerializer
    queryset=Ratings.objects.all()
    @swagger_auto_schema(operation_summary="Add ratings to database")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class RatinDetailiew(generics.GenericAPIView):
    serializer_class=serializers.RatingCreationSerializer
    queryset=Ratings.objects.all()
    @swagger_auto_schema(operation_summary="Fetch ratings by product id")
    def get(self, request,product_id):
        rating=Ratings.objects.all().filter(product=product_id)
        serializer=self.serializer_class(instance=rating,many=True)
        if serializer.data:
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data="Data not found",status=status.HTTP_204_NO_CONTENT)