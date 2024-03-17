# from rest_framework import status
# from rest_framework.mixins import CreateModelMixin
# from rest_framework.response import Response
from rest_framework.viewsets import  ModelViewSet

from models import Products
from product.serializers import ProductsSerializers

class ProductViewSet(ModelViewSet):
    serializer_class = ProductsSerializers

    def get_queryset(self):
        return Products.objects.all()