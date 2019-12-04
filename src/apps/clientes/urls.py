from .views import ClientViewSet, ProductViewSet
from django.urls import path, include
from rest_framework import routers

# O trailing_slash serve para ignorarmos a barra final ao testar no Postman,
# entre outros
router = routers.DefaultRouter(trailing_slash=False)
# Aqui vai a rota
router.register('clients', ClientViewSet)
router.register('product', ProductViewSet)

'''
Qual a diferença entre put e patch?
No patch você altera vários valores, no put é recomendado para um apenas.
'''

app_name = 'clientes'
urlpatterns = [
    path('', include(router.urls))
]
