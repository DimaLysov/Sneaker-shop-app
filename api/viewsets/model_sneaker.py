from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import ModelSneaker
from api.serializers.model_sneaker import ModelSneakerSerializer

@extend_schema(tags=['ModelSneaker'])
class ModelSneakerViewSet(ReadOnlyModelViewSet):
    serializer_class = ModelSneakerSerializer
    queryset = ModelSneaker.objects.all()
