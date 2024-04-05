
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import  ModelViewSet

from product.models import Products
from product.serializers import ProductsSerializers

class ProductViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializers
    queryset         = Products.objects.all().order_by('id')

    def get_queryset(self):
        return super().get_queryset()
    