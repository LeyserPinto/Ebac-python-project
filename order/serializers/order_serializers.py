from rest_framework import serializers

from product.models import Products
from product.serializers.products_serializers import ProductsSerializers


class OrderSerializers(serializers.ModelSerializer):
    products = ProductsSerializers(required = True, many = True)
    total    = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([products.price for products in instance.products.all])
        return total
    
    class  Meta:
        model = Products
        fields = ['products', 'total']