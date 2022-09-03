from django.contrib.auth import get_user_model
from django.shortcuts import render,get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import Cart

User=get_user_model()
# Create your views here.
class CartCreateListView(generics.GenericAPIView):
    
    serializer_class=serializers.CartCreationSerializer
    queryset=Cart.objects.all()
    @swagger_auto_schema(operation_summary="Fetch all cart")
    def get(self, request):
        cart=Cart.objects.all()
        serializer=self.serializer_class(instance=cart,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Add product to a cart")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CartDetailView(generics.GenericAPIView):
    serializer_class=serializers.CartCreationSerializer
    
    @swagger_auto_schema(operation_summary="Delete product from cart by id")
    def delete(self,request,cart_id):
        cart=get_object_or_404(Cart,pk=cart_id)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateQuantityView(generics.GenericAPIView):
    serializer_class=serializers.ProductQuantityUpdateSerializer
    @swagger_auto_schema(operation_summary="Update the quantity of products in cart")
    def put(self,request,cart_id):
        cart=get_object_or_404(Cart,pk=cart_id)
        data=request.data
        serializer=self.serializer_class(data=data,instance=cart)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
            
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  