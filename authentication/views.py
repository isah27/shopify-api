from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import check_password
from .models import User
from . import serializers


# Create your views here.
class HelloAuthView(generics.GenericAPIView):
    def get(self,requests):
        return Response(data={"message":"Hello Auth"}, status=status.HTTP_200_OK)
    
class UserCreateView(generics.GenericAPIView):
    serializer_class=serializers.UserCreationSerialiser
    queryset=User.objects.all()
    @swagger_auto_schema(operation_summary="Create a new user")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Fetch all the user")
    def get(self,request):
        user=User.objects.all()
        serializer=self.serializer_class(instance=user,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
   
class UserLoginView(generics.GenericAPIView):
    serializer_class=serializers.UserDetailSerializer
    queryset=User.objects.all()
    @swagger_auto_schema(operation_summary="Login with email and password. If the info exist, A text 'Accepted' will be return with a status code 200")
    def get(self,request,email,password):
        user=User.objects.all().filter(email=email)
        serializer=self.serializer_class(instance=user,many=True)
        if serializer.data:
            if check_password(password=password,encoded=serializer.data[0]['password']):
                return Response(data="Accepted",status=status.HTTP_200_OK)
            return Response(data="Wrong Password",status=status.HTTP_401_UNAUTHORIZED)
        return Response(data="User not found!",status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailView(generics.GenericAPIView):
    serializer_class=serializers.UserDetailSerializer
    queryset=User.objects.all()
    @swagger_auto_schema(operation_summary="Fetch a specific user by id")
    def put(self, request,user_id):
        data=request.data
        user=get_object_or_404(User,pk=user_id)
        serializer=self.serializer_class(data=data,instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
            
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(operation_summary="Delete a user by id")
    def delete(self, request,user_id):
        product=get_object_or_404(User,pk=user_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    