from rest_framework import serializers

from api.models import SKU


class SKUSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='model_sneaker.name')
    brand = serializers.CharField(source='model_sneaker.brand.name')
    color  = serializers.CharField(source='model_sneaker.color')
    size = serializers.CharField(source='size.__str__')
    image_url = serializers.CharField(source='model_sneaker.image_url')
    class Meta:
        model = SKU
        fields = ['id', 'brand', 'name', 'color', 'size', 'image_url', 'price']
