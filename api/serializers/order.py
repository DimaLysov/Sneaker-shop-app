from rest_framework import serializers

from api.models import Order
from api.serializers.item_order import ItemOrderAllDataSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderGetNewOrderSerializer(serializers.ModelSerializer):
    user_tg_id = serializers.CharField(source='user.tg_id')
    items = ItemOrderAllDataSerializer(many=True, source='itemorder_set')

    class Meta:
        model = Order
        fields = ['user_tg_id', 'fullname', 'phone_number', 'delivery_address', 'items']