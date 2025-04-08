from rest_framework import serializers

from api.models import SKU


class SKUSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='model_sneaker.model_name')  # Получаем имя кроссовок из связанных моделей
    brand = serializers.CharField(source='model_sneaker.brand.brand_name')  # Предполагается, что в модели Sneaker есть связь с Brand
    image_url = serializers.CharField(source='model_sneaker.image_url')
    class Meta:
        model = SKU
        fields = ['id', 'name', 'price', 'brand', 'image_url']
