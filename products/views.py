import os
from django.contrib.auth import get_user_model
from django.shortcuts import render,get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import Products
from django.http import HttpResponse

User=get_user_model()
# Create your views here.

class ProductCreateListView(generics.GenericAPIView):
    
    serializer_class=serializers.ProductCreationSerializer
    queryset=Products.objects.all()
    
    @swagger_auto_schema(operation_summary="Fetch all product")
    def get(self, request):
        product=Products.objects.all()
        serializer=self.serializer_class(instance=product,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Add product")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailView(generics.GenericAPIView):
    serializer_class=serializers.ProductDetailSerializer
    
    @swagger_auto_schema(operation_summary="fetch product by id")
    def get(self, request,product_id):
        product=get_object_or_404(Products,pk=product_id)
        img=product.image.path
        return HttpResponse(img)
        # serializer=self.serializer_class(instance=product)
        # return Response(data=serializer.data,status=status.HTTP_200_OK)
        
    @swagger_auto_schema(operation_summary="Update product by id")
    def put(self, request,product_id):
        data=request.data
        product=get_object_or_404(Products,pk=product_id)
        serializer=self.serializer_class(data=data,instance=product)
        if serializer.is_valid():
                # check if the incoming data has image
                if len(data["image"])>0:
                    # delete the formal image if the incoming data has image
                    try:
                        os.remove(product.image.path)
                    except:
                        pass
                    # save it
                    serializer.save()
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                # assign the previous image to incoming data if it doesn't have
                serializer.validated_data["image"]=product.image
                # then save it
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Delete product by id")
    def delete(self, request,product_id):
        product=get_object_or_404(Products,pk=product_id)
        # delete the image fro image folif len(product.image)>0:
        try:
            os.remove(product.image.path)
        except:
            pass
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserProductView(generics.GenericAPIView):
    serializer_class=serializers.ProductDetailSerializer
    
    @swagger_auto_schema(operation_summary="fetch product by vendor/seller id")
    def get(self,request,vendor_id):
        user=User.objects.get(pk=vendor_id)
        product=Products.objects.all().filter(vendor=user)
        serializer=self.serializer_class(instance=product,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
       
        
    