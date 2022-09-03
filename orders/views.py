from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .models import Order
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers


# Create your views here.
    
class OrderCreateListView(generics.GenericAPIView):
    serializer_class=serializers.OrderCreationSerializer
    queryset=Order.objects.all()
    
    @swagger_auto_schema(operation_summary="Fetch all orders")
    def get(self,request):
        order=Order.objects.all()
        serializer=self.serializer_class(instance=order,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="add product to order table")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class OrderDetailView(generics.GenericAPIView):
    serializer_class=serializers.OrderDetailSerializer
    
    @swagger_auto_schema(operation_summary="update order by id")
    def put(self,request,order_id):
        data=request.data
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
            
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Delete order by id")
    def delete(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class=serializers.OrderStatusUpdateSerializer
    
    @swagger_auto_schema(operation_summary="update order status by id")
    def put(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        data=request.data
        serializer=self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
            
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
class CustomerOrderView(generics.GenericAPIView):
    serializer_class=serializers.OrderDetailSerializer
    @swagger_auto_schema(operation_summary="Fetch order by customer id for a specific customer")
    def get(self,request,customer_id):
        order=Order.objects.all().filter(customer=customer_id)
        serializer=self.serializer_class(instance=order,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
       
