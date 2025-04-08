from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Brand
from api.serializers.brand import BrandSerializer

@extend_schema_view(
    list=extend_schema(
        description="Получение списка всех брендов",
        summary="Список брендов",
    ),
    retrieve=extend_schema(
        description="Получение информации о конкретном бренде по ID",
        summary="Информация о бренде",
    ),
)
@extend_schema(tags=['Brand'])
class BrandViewSet(ReadOnlyModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
