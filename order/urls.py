from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .viewsets import OrderViewSet

router = SimpleRouter()
router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = [
    path('', include(router.urls)),
]

