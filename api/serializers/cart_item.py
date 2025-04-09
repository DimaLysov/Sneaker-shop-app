from rest_framework import serializers

from api.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'sku', 'quantity']


class CartItemUpdateSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    class Meta:
        model = CartItem
        fields = ['quantity']

    def update(self, instance, validated_data):
        instance.quantity = validated_data['quantity']
        instance.save()
        return instance