from django.contrib import admin
from restaurante.models import Cardapio

class ListandoCardapio(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "preco", "imagem")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 10

admin.site.register(Cardapio, ListandoCardapio)
