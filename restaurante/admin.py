from django.contrib import admin
from restaurante.models import Cardapio

class ListandoCardapio(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "preco", "imagem")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)

admin.site.register(Cardapio, ListandoCardapio)
