from django.db import models

class Cardapio(models.Model):
    
    OPCOES_CATEGORIA = [
        ("BEBIDA", "Bebida"),
        ("PRATO PRINCIPAL", "Prato principal"),
        ("SOBREMESA", "Sobremesa")
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to="fotos/%Y/%m/%d/", height_field=None, width_field=None, max_length=None, blank=True)
    publicado = models.BooleanField(default=False)
