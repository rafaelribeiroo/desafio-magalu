from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
router.register('clients', CategoryViewSet)

'''
Qual a diferença entre put e patch?
No patch você altera vários valores, no put é recomendado para um apenas.
'''

app_name = 'clientes'
urlpatterns = [
    path('', include(router.urls))
]
