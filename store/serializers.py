from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_total']
    product_total = serializers.SerializerMethodField(method_name='products_by_collection')

    def products_by_collection(self, collection: Collection):
        return Product.objects.filter(collection=collection).count()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['confirm_password']:
    #         return serializers.ValidationError('Passwords do not match')
    #     return attrs
