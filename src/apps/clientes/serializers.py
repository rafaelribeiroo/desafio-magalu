from rest_framework import serializers
from .models import Client

'''
O que é a serialização? Serializar uma informação seria...
Simplificando ao máximo, seria "converter" informações e modelos em JSON.
'''


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        # Diretiva que reune todas as colunas nesse caso
        fields = '__all__'
