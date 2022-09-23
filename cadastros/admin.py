from django.contrib import admin

#Importar as classes
from .models import Estado, Cidade, Categoria, Produto, Estabelecimento, Venda

# Register your models here.
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Estabelecimento)
admin.site.register(Venda)
