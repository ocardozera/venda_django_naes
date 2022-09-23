from unicodedata import decimal
from django.db import models

# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return "{} - {}".format(self.nome, self.sigla)

class Cidade(models.Model):
    nome = models.CharField(max_length=150)
    
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.nome, self.estado.nome)

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return "{}".format(self.nome)        

class Produto(models.Model):
    nome = models.CharField(max_length=150)

    preco = models.DecimalField(decimal_places=2, max_digits=5)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.nome, self.categoria.nome)

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=200)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14)
    cpf = models.CharField(max_length=11)

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}/{}".format(self.nome, self.cidade.nome, self.cidade.estado.nome)


class Venda(models.Model):
    valor_total = models.DecimalField(decimal_places=2, max_digits=5)
    valor_final = models.DecimalField(decimal_places=2, max_digits=5)
    desconto = models.DecimalField(decimal_places=2, max_digits=5)
    
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT) 

    def __str__(self):
        return "Valor Total: R$ {} - Valor Final: R$ {} - {}".format(self.valor_total, self.valor_final, self.estabelecimento.nome)


