#Importar o TemplateView para criar páginas simples
from django.views.generic import TemplateView

# A classe IndexView "extends" TemplateView
class IndexView(TemplateView):
    # Toda classe filha do TemplateView precisa
    # do atributo abaixo para definir um template à ser renderizado
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"