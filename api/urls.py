from django.urls import path, include
from rest_framework import routers

from .viewsets.brand import BrandViewSet
from .viewsets.model_sneaker import ModelSneakerViewSet
from .viewsets.sku import SKUViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'model-sneakers', ModelSneakerViewSet)
router.register(r'skus', SKUViewSet, basename='sku')

urlpatterns = [
    path('', include(router.urls)),
]
