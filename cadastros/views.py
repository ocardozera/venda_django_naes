from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Estabelecimento, Estado, Cidade, Categoria, Produto, Venda

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.


class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Estado'
        context['botaoSalvar'] = 'Cadastrar'

        return context


class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estado
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Editar Estado'
        context['botaoSalvar'] = 'Salvar'

        return context

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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Cidade'
        context['botaoSalvar'] = 'Cadastrar'

        return context


class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Editar Cidade'
        context['botaoSalvar'] = 'Salvar'

        return context

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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Categoria'
        context['botaoSalvar'] = 'Cadastrar'

        return context

class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Editar Categoria'
        context['botaoSalvar'] = 'Salvar'

        return context


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Produto'
        context['botaoSalvar'] = 'Cadastrar'

        return context


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    fields = ['nome', 'preco', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Editar Produto'
        context['botaoSalvar'] = 'Salvar'

        return context


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
    fields = ['nome', 'logradouro', 'numero', 'bairro', 'cnpj', 'cpf', 'cep', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estabelecimento')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Estabelecimento'
        context['botaoSalvar'] = 'Cadastrar'

        return context


class EstabelecimentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Estabelecimento
    fields = ['nome', 'logradouro', 'numero',
              'bairro', 'cnpj', 'cpf', 'cep','cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estabelecimento')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Editar Estabelecimento'
        context['botaoSalvar'] = 'Salvar'

        return context


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Criar Venda'
        context['botaoSalvar'] = 'Cadastrar'

        return context

    def form_valid(self, form):
        
        # Antes do super não foi criado o obj

        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        # Depois do super o obj está criado
         
        return url

class VendaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Venda
    fields = ['produto', 'valor_total',
              'valor_final', 'desconto', 'estabelecimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-venda')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Editar Venda'
        context['botaoSalvar'] = 'Salvar'

        return context

    def get_object(self, queryset=None): 
        # get_object_or_404(Classe, atrr='isso')

        self.object = get_object_or_404(Venda, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class VendaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Venda
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-venda')

    def get_object(self, queryset=None):
        # get_object_or_404(Classe, atrr='isso')

        self.object = get_object_or_404(
            Venda, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class VendaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Venda
    template_name = 'cadastros/listas/venda.html'

    def get_queryset(self):
        self.object_list = Venda.objects.filter(usuario=self.request.user)
        return self.object_list

################### UPDATE ###################

