from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import CustomUserTokenSerializer,UserSerializer, OrderItemsByOrderIdSerializer,CompanySerializer, CategorySerializer, ProductSerializer, OrderSerializer, OrderItemsSerializer
from rest_framework.response import Response
from .models import Company, Category, Product, Order, OrderItems
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import action

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': CustomUserTokenSerializer(user, context={'request': request}).data
    }

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

    @action(detail=True, methods=['GET'])
    def orderItems(self, request, pk=None):
        order = self.get_object()
        orderItems = OrderItems.objects.filter(order=order)
        serializer = OrderItemsByOrderIdSerializer(orderItems, many=True)
        return Response(serializer.data,status=200)

    @action(detail=True, methods=['POST'])
    def orderItemsSave(self, request, pk=None):
        order = self.get_object()
        data = request.data
        for objectItem in data:
            objectItem['order'] = order.id
            serializer = OrderItemsByOrderIdSerializer(data=objectItem)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data,status='201')

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
