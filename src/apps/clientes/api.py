from .serializers import ClientSerializer
from rest_framework import viewsets
from .models import Category

# Ao disponibilizar um recurso, a classe é mais apropriada que várias funções,
# pois ficam agrupadas todas as operações que oferecemos.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Category.objects.all()
