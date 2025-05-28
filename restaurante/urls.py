from django.urls import path, include
from restaurante.views import index, cardapio

urlpatterns = [
    path('', index, name='index'),
    path('cardapio/', cardapio, name='cardapio')
]