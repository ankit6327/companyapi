from rest_framework import serializers
from .models import Company, Category, Product, Order,OrderItems 
from django.contrib.auth.models import User
from django.http import HttpResponse


class CustomUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','is_staff','is_active']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OrderItemsByOrderIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['id','product', 'order', 'qty']

class ProductSerializer(serializers.ModelSerializer):
    user = CustomUserTokenSerializer(source='createdBy', read_only='True')
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'createdBy', 'user']

class OrderSerializer(serializers.ModelSerializer):
    user = CustomUserTokenSerializer(source='createdBy', read_only='True')
    class Meta:
        model = Order
        fields = ['id','status', 'createdDate','createdBy', 'user']
        
class OrderItemsSerializer(serializers.ModelSerializer):
    order = OrderSerializer(source='order', read_only='True')
    class Meta:
        model = OrderItems
        fields = ['id','product', 'order', 'qty']

