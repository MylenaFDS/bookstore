from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .viewsets import ProductViewSet, CategoryViewSet

router = SimpleRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"categories", CategoryViewSet, basename="categories")

urlpatterns = [
    path('', include(router.urls)),
]

