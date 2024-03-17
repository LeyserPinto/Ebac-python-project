from django.urls import path, include
from rest_framework import routers

from .viewset import OrderViewSet

router = routers.SimpleRouter()
router.register(r'order', OrderViewSet, basename='order')

urlpattners = [
    path('', include(router.urls))
]