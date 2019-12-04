from .serializers import ClientSerializer, ProductSerializer
from rest_framework import viewsets
from .models import Client, Product

# Ao disponibilizar um recurso, a classe é mais apropriada que várias funções,
# pois ficam agrupadas todas as operações que oferecemos.


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
