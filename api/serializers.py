from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['name', 'price', 'noshares']

class StockNameSerializer(serializers.ModelSerializer):
        name = serializers.CharField(max_length=36)

