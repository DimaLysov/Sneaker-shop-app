from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import SKU
from api.serializers.sku import SKUSerializer

@extend_schema(tags=['SKU'])
@extend_schema_view(
    list=extend_schema(
        summary="Получить все записи из sku",
    ),
    retrieve=extend_schema(
        summary="Получить конкретную запись по ее id",
    ),
)
class SKUViewSet(ReadOnlyModelViewSet):
    serializer_class = SKUSerializer
    queryset = SKU.objects.all()
