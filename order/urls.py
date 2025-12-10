from django.urls import include, path
from rest_framework import routers
from order import viewsets

router = routers.DefaultRouter()
router.register(r"order", viewsets.OrderViewSet, basename="orders")

urlpatterns = [
    path("", include(router.urls)),
]


