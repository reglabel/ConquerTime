from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    dados = DadosEmpresas.objects.all()
    produtos = Produto.objects.all()
    pessoas = Pessoa.objects.all()
    sede = DadosSede.objects.all()

    dicionario = {
        "dados_site": dados,
        "lista_produtos" : produtos,
        "lista_pessoas" : pessoas,
        "info_sede": sede[0]
    }

    return render(request, "index.html", dicionario)