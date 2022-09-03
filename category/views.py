from django.shortcuts import get_object_or_404
from rest_framework import generics,status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from . import serializers
from .models import Category

# Create your views here.
class CategoryCreateListView(generics.GenericAPIView):
    serializer_class=serializers.CategorySerializer
    queryset=Category.objects.all()
    @swagger_auto_schema(operation_summary="Create a category. note(if a category is deleted all the products in that catagory will be deleted automatically).")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data="Created",status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Fetch all the category")
    def get(self, requst):
        category=Category.objects.all()
        serializer=self.serializer_class(instance=category,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class CategoryDetailView(generics.GenericAPIView):
    serializer_class=serializers.CategorySerializer
    
    @swagger_auto_schema(operation_summary="Update category")
    def put(self,request,category_id):
        data=request.data
        category=get_object_or_404(Category,pk=category_id)
        serializer=self.serializer_class(data=data,instance=category)
        if serializer.is_valid():
            serializer.save()
            return Response(data="Update successfully",status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Delete catagory")
    def delete(self,request,category_id):
        category=get_object_or_404(Category,pk=category_id)
        category.delete()
        return Response(data="Deleted",status=status.HTTP_204_NO_CONTENT)
