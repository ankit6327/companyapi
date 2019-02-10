from django.contrib import admin
from django.urls import path, include
from .views import CompanyViewSet, CategoryViewSet, ProductViewSet, OrderViewSet, OrderItemsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderItem', OrderItemsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
