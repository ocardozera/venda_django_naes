from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Estabelecimento, Estado, Cidade, Categoria, Produto, Venda

from django.urls import reverse_lazy

# Create your views here.
class EstadoCreate(CreateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')


class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

class EstadoDelete(DeleteView):
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')

class EstadoList(ListView):
    model = Estado
    template_name = 'cadastros/listas/estado.html'

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')


class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/listas/cidade.html'

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')


class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')

class CategoriaList(ListView):
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome', 'preco', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome', 'preco', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')

class ProdutoList(ListView):
    model = Produto
    template_name = 'cadastros/listas/produto.html'

class EstabelecimentoCreate(CreateView):
    model = Estabelecimento
    fields = ['nome', 'logradouro', 'numero', 'bairro', 'cnpj', 'cpf', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estabelecimento')

class EstabelecimentoUpdate(UpdateView):
    model = Estabelecimento
    fields = ['nome', 'logradouro', 'numero',
              'bairro', 'cnpj', 'cpf', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estabelecimento')


class EstabelecimentoDelete(DeleteView):
    model = Estabelecimento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estabelecimento')

class EstabelecimentoList(ListView):
    model = Estabelecimento
    template_name = 'cadastros/listas/estabelecimento.html'

class VendaCreate(CreateView):
    model = Venda
    fields = ['produto', 'valor_total', 'valor_final', 'desconto', 'estabelecimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')


class VendaUpdate(UpdateView):
    model = Venda
    fields = ['produto', 'valor_total',
              'valor_final', 'desconto', 'estabelecimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')


class VendaDelete(DeleteView):
    model = Venda
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-venda')


class VendaList(ListView):
    model = Venda
    template_name = 'cadastros/listas/venda.html'

################### UPDATE ###################

