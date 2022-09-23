from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Estabelecimento, Estado, Cidade, Categoria, Produto, Venda

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.


class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')


class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')


class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')


class EstadoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estado
    template_name = 'cadastros/listas/estado.html'


class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')


class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')


class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')


class CidadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Cidade
    template_name = 'cadastros/listas/cidade.html'


class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')


class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')


class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')


class CategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'


class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    fields = ['nome', 'preco', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    fields = ['nome', 'preco', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')


class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')


class ProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    template_name = 'cadastros/listas/produto.html'


class EstabelecimentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estabelecimento
    fields = ['nome', 'logradouro', 'numero', 'bairro', 'cnpj', 'cpf', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estabelecimento')


class EstabelecimentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estabelecimento
    fields = ['nome', 'logradouro', 'numero',
              'bairro', 'cnpj', 'cpf', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estabelecimento')


class EstabelecimentoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estabelecimento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estabelecimento')


class EstabelecimentoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estabelecimento
    template_name = 'cadastros/listas/estabelecimento.html'


class VendaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Venda
    fields = ['produto', 'valor_total', 'valor_final', 'desconto', 'estabelecimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')


class VendaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Venda
    fields = ['produto', 'valor_total',
              'valor_final', 'desconto', 'estabelecimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')


class VendaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Venda
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-venda')


class VendaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Venda
    template_name = 'cadastros/listas/venda.html'

################### UPDATE ###################

