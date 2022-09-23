from django.urls import path

# Importa as views que a gente criou
from .views import IndexView, SobreView

urlpatterns = [
    #Todo path tem endereço, sua_view.as_view() e nome
    # path('endereço/', MinhaView.as_view(), name='nome-da-url'),
    
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]