from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import SKU
from api.serializers.sku import SKUSerializer

@extend_schema(tags=['SKU'])
class SKUViewSet(ReadOnlyModelViewSet):
    serializer_class = SKUSerializer
    queryset = SKU.objects.all()
