from django.db.models import Sum
from rest_framework import serializers
from .models import Product, Category


class ProductListSerializer(serializers.ModelSerializer):
    """List products"""
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category', 'price', 'count')


class ProductDetailSerializer(serializers.ModelSerializer):
    """Detail product"""
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'count')


class CategoryListSerializer(serializers.ModelSerializer):
    """List category"""

    def get_sum(self, obj):
        return Product.objects.filter(category=obj).aggregate(Sum('count'))

    sum_count = serializers.SerializerMethodField('get_sum')

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'sum_count')


class CRUDProductSerializer(serializers.ModelSerializer):
    """crud for product"""
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category', 'price', 'count')


class CRUDCategorySerializer(serializers.ModelSerializer):
    """crud for category"""
    class Meta:
        model = Category
        fields = ('id', 'title', 'description')

