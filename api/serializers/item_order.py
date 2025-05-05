from rest_framework import serializers

from api.models import ItemOrder


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrder
        fields = '__all__'