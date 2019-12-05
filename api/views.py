from .serializers import ClientSerializer, ProductSerializer
from rest_framework import viewsets
from rest_framework import pagination
from .models import Client, Product

# Ao disponibilizar um recurso, a classe é mais apropriada que várias funções,
# pois ficam agrupadas todas as operações que oferecemos.


class Pagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    # Lista dos mais recentes aos mais antigos
    queryset = Client.objects.all().order_by('-id')
    pagination_class = Pagination


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
