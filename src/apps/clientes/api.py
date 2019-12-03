from .serializers import ClientSerializer
from rest_framework import viewsets

# Ao disponibilizar um recurso, a classe é mais apropriada que várias funções,
# pois ficam agrupadas todas as operações que oferecemos.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    # não retorna a consulta, mas um queryset
    queryset = Category.objects.all()
