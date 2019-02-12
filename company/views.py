from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import UserSerializer, CompanySerializer,CategorySerializer,ProductSerializer,OrderSerializer,OrderItemsSerializer
from rest_framework.response import Response 
from .models import Company, Category, Product, Order, OrderItems 
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
  