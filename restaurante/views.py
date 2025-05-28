from django.shortcuts import render
from restaurante.models import Cardapio

def index(request):
    return render(request, 'restaurante/index.html')

def cardapio(request):
    cardapio = Cardapio.objects.all()
    return render(request, 'restaurante/cardapio.html', {"cardapio":cardapio})
