from django.contrib import admin
from restaurante.models import Cardapio

class ListandoCardapio(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "categoria", "publicado", "imagem")
    list_display_links = ("id", "nome")
    list_filter = ("categoria",)
    list_editable = ("publicado",)
    search_fields = ("nome",)
    list_per_page = 10

admin.site.register(Cardapio, ListandoCardapio)
