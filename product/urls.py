from django.urls import path, include
from rest_framework import routers

from viewset import ProductViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpattners = [
    path('', include(router.urls))
]