from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.viewsets.product_viewset import ProductViewSet
from product.viewsets.category_viewset import CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]

