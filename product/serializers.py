from rest_framework import serializers
from .models import Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
