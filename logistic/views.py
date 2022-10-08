from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

#TODO Получение списка продуктов, поиск продуктов по названию, описанию. Добавление/обновление/удаление продуктов
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'description']
    search_fields = ['title', 'description']
    ordering_fields = ['id']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['products']
    ordering_fields = ['id']