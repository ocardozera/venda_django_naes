from django.urls import path

# Importa as views que a gente criou
from .views import EstadoCreate, CidadeCreate, CategoriaCreate, EstabelecimentoCreate, ProdutoCreate, VendaCreate
from .views import EstadoUpdate, CidadeUpdate, CategoriaUpdate, EstabelecimentoUpdate, ProdutoUpdate, VendaUpdate
from .views import EstadoDelete, CidadeDelete, CategoriaDelete, EstabelecimentoDelete, ProdutoDelete, VendaDelete
from .views import EstadoList, CidadeList, CategoriaList, EstabelecimentoList, ProdutoList, VendaList

urlpatterns = [
    #Todo path tem endereço, sua_view.as_view() e nome
    # path('endereço/', MinhaView.as_view(), name='nome-da-url'),

    path('cadastros/estado/', EstadoCreate.as_view(), name='cadastros-estado'),
    path('cadastros/cidade/', CidadeCreate.as_view(), name='cadastros-cidade'),
    path('cadastros/categoria/', CategoriaCreate.as_view(), name='cadastros-categoria'),
    path('cadastros/produto/', ProdutoCreate.as_view(), name='cadastros-produtos'),
    path('cadastros/estabelecimento/', EstabelecimentoCreate.as_view(), name='cadastros-estabelecimento'),
    path('cadastros/venda/', VendaCreate.as_view(), name='cadastros-venda'),

    path('editar/estado/<int:pk>', EstadoUpdate.as_view(), name='editar-estado'),
    path('editar/cidade/<int:pk>', CidadeUpdate.as_view(), name='editar-cidade'),
    path('editar/categoria/<int:pk>', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/produto/<int:pk>', ProdutoUpdate.as_view(), name='editar-produto'),
    path('editar/estabelecimento/<int:pk>', EstabelecimentoUpdate.as_view(), name='editar-estabelecimento'),
    path('editar/venda/<int:pk>', VendaUpdate.as_view(), name='editar-venda'),

    path('excluir/estado/<int:pk>', EstadoDelete.as_view(), name='excluir-estado'),
    path('excluir/cidade/<int:pk>', CidadeDelete.as_view(), name='excluir-cidade'),
    path('excluir/categoria/<int:pk>', CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/produto/<int:pk>', ProdutoDelete.as_view(), name='excluir-produto'),
    path('excluir/estabelecimento/<int:pk>', EstabelecimentoDelete.as_view(), name='excluir-estabelecimento'),
    path('excluir/venda/<int:pk>', VendaDelete.as_view(), name='excluir-venda'),

    path('listar/estado', EstadoList.as_view(), name='listar-estado'),
    path('listar/cidade', CidadeList.as_view(), name='listar-cidade'),
    path('listar/categoria', CategoriaList.as_view(), name='listar-categoria'),
    path('listar/produto', ProdutoList.as_view(), name='listar-produto'),
    path('listar/estabelecimento', EstabelecimentoList.as_view(), name='listar-estabelecimento'),
    path('listar/venda', VendaList.as_view(), name='listar-venda')
]
