from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Size
from api.serializers.size import SizeSerializer

@extend_schema(tags=['Size'])
class SizeViewSet(ReadOnlyModelViewSet):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()
