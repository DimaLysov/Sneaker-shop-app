from django.urls import path, include
from rest_framework import routers

from .viewsets.brand import BrandViewSet
from .viewsets.model_sneaker import ModelSneakerViewSet
from .viewsets.sku import SKUViewSet
from .viewsets.size import SizeViewSet
from .viewsets.cart_item import CartItemViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'model-sneakers', ModelSneakerViewSet)
router.register(r'skus', SKUViewSet, basename='sku')
router.register(r'sizes', SizeViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
