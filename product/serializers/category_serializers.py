from rest_framework import serializers

from models.category import Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active',
        ]