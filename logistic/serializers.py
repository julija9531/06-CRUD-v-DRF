from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']



class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']


    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # Заполняем таблицу StockProduct
        for pos in positions:
            StockProduct(stock=stock, product=pos.get('product'), quantity=pos.get('quantity'), price=pos.get('price')).save()

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # Обновляем таблицу StockProduct
        StockProduct.objects.filter(stock=stock).delete()
        for pos in positions:
            StockProduct(stock=stock, product=pos.get('product'), quantity=pos.get('quantity'), price=pos.get('price')).save()

        return stock
