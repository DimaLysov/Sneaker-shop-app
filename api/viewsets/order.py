from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Order
from api.serializers.order import OrderSerializer, OrderGetNewOrderSerializer

@extend_schema(tags=['Order'])
@extend_schema_view(
    list=extend_schema(
        summary="Получить все заказы",
    ),
)
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    @action(detail=False, methods=['get'], url_path='new-order', serializer_class=OrderGetNewOrderSerializer)
    def get_new_order(self, request):
        new_orders = self.queryset.filter(status='new')
        serializer = self.serializer_class(new_orders, many=True)
        answer = serializer.data
        self.queryset.update(status='processing')
        return Response(answer)