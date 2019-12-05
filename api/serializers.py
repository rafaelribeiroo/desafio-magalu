from rest_framework import serializers
from .models import Client, Product

'''
O que é a serialização? Serializar uma informação seria...
Simplificando ao máximo, seria "converter" informações e modelos em JSON.
'''


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id', 'title']  # 'price', 'image', 'brand', 'reviewScore'


class ClientSerializer(serializers.ModelSerializer):
    favorite = ProductSerializer(read_only=True, many=True)
    favorite_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        source='favorite',
        many=True
    )

    class Meta:
        model = Client
        # fields = '__all__'
        fields = ('id', 'name', 'email', 'favorite', 'favorite_id')
