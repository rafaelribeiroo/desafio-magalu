from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet

# O trailing_slash serve para ignorarmos a barra final ao testar no Postman,
# entre outros
router = routers.DefaultRouter(trailing_slash=False)
# Aqui vai a rota
router.register('clients', CategoryViewSet)

'''
Qual a diferença entre put e patch?
No patch você altera vários valores, no put é recomendado para um apenas.
'''

app_name = 'clientes'
urlpatterns = [
    path('', include(router.urls))
]
