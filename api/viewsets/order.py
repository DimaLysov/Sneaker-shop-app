from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from api.models import Order
from api.serializers.order import OrderSerializer

@extend_schema(tags=['Order'])
@extend_schema_view(
    list=extend_schema(
        summary="Получить все заказы",
    ),
)
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()