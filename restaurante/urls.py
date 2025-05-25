from django.urls import path, include
from restaurante.views import index

urlpatterns = [
    path('', index, name='index')
]