import email
from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.hashers import make_password, check_password

class UserCreationSerialiser(serializers.ModelSerializer):
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    phone_number=PhoneNumberField(allow_null=False,allow_blank=False)
    gender=serializers.CharField(max_length=10)
    address=serializers.CharField()
    bank_names=serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    account_names=serializers.CharField(max_length=100,allow_blank=True,allow_null=True)
    account_numbers=serializers.CharField(allow_blank=True,allow_null=True,max_length=20)
    account_types=serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    password=serializers.CharField(min_length=6)
    
    class Meta:
        model=User
        fields=['id','username','email','phone_number','gender','address','bank_names','account_names','account_numbers','account_types',
                'password']
    def validate(self,attrs):
        username_exist=User.objects.filter(username=attrs['username']).exists()
        
        if username_exist:
            raise serializers.ValidationError(detail="User with username exist")
        
        email_exist=User.objects.filter(email=attrs['email']).exists()
        
        if email_exist:
            raise serializers.ValidationError(detail="User with email exist")
        
        phone_number_exist=User.objects.filter(phone_number=attrs['phone_number']).exists()
        
        if phone_number_exist:
            raise serializers.ValidationError(detail="User with phone_number exist")
        
        
        return super().validate(attrs)
    
    def create(self,validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            gender=validated_data['gender'],
            address=validated_data['address'],
            bank_names=validated_data['bank_names'],
            account_names=validated_data['account_names'],
            account_numbers=validated_data['account_numbers'],
            account_types=validated_data['account_types'],
            password=make_password(validated_data['password']),
            )
        user.save()
        return user
    
class UserDetailSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=100)
    phone_number=PhoneNumberField(allow_null=False,allow_blank=False)
    gender=serializers.CharField(max_length=10)
    address=serializers.CharField()
    bank_names=serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    account_names=serializers.CharField(max_length=100,allow_blank=True,allow_null=True)
    account_numbers=serializers.CharField(allow_blank=True,allow_null=True,max_length=20)
    account_types=serializers.CharField(max_length=50,allow_blank=True,allow_null=True)
    password=serializers.CharField(min_length=6)
    
    class Meta:
        model=User
        fields=['id','username','email','phone_number','gender','address','bank_names','account_names','account_numbers','account_types',
                'password']