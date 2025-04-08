from rest_framework import serializers

from api.models import ModelSneaker


class ModelSneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelSneaker
        fields = '__all__'
