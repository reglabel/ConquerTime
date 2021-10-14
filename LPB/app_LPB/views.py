from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    categorias = Categoria.objects.all()
    tarefas = Tarefa.objects.all()
    sede = DadosSede.objects.all()

    dicionario = {
        "lista_categorias": categorias,
        "lista_tarefas" : tarefas,
        "info_sede": sede[0]
    }

    return render(request, "index.html", dicionario)