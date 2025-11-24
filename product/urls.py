from django.urls import include, path
from rest_framework import routers
from product import viewsets

router = routers.DefaultRouter()
router.register(r"products", viewsets.ProductViewSet, basename="products")
router.register(r"categories", viewsets.CategoryViewSet, basename="categories")

urlpatterns = [
    path("", include(router.urls)),
]

