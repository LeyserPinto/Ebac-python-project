from rest_framework import serializers

from models.products import Products
from serializers.category_serializers import CategorySerializers

class ProductsSerializers(serializers.ModelSerializer):
    category = CategorySerializers(required = True, many = True)

    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price',
            'active',
            'category',
        ]