from rest_framework import serializers


from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer
from django.contrib.auth.models import User


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)  # CORREÇÃO
    total = serializers.SerializerMethodField()
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    def get_total(self, instance):
        return sum(product.price for product in instance.product.all())

    class Meta:
        model = Order
        fields = ["product", "total", "user", "products_id"]

    def create(self, validated_data):
        product_data = validated_data.pop("products_id")
        user_data = validated_data.pop("user")

        order = Order.objects.create(user=user_data)
        order.product.set(product_data)
        return order