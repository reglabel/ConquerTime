from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
#from django.core.paginator import Paginator
from .models import Tarefa, Categoria
from .forms import TarefaForm, CategoriaForm

# Create your views here.

def cadastroTarefa(request):
    categorias = Categoria.objects.all()
    tarefas = Tarefa.objects.all()
    sede = DadosSede.objects.all()

    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            try:
                instance = form.save()
                instance.save()
                return redirect('cronometro', id=instance.id)
            except:
                print(request, "Erro ao cadastrar a tarefa!")

    form = TarefaForm()
    dados = {
        'form': form,
        "lista_categorias": categorias,
        "lista_tarefas" : tarefas,
        "info_sede": sede[0]
    }
    return render(request, 'cadastrar_tarefa.html', dados)

def excluirTarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if tarefa:
        tarefa.delete()
        return redirect('home')
    else:
        return redirect('home')

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

def cronometro(request, id):
    tarefaDaVez = Tarefa.objects.get(id=id)
    categorias = Categoria.objects.all()
    tarefas = Tarefa.objects.all()
    sede = DadosSede.objects.all()

    dicionario = {
        "lista_categorias": categorias,
        "lista_tarefas" : tarefas,
        "info_sede": sede[0],
        'tarefa': tarefaDaVez
    }
    return render(request, "cronometro.html", dicionario)

def relatorioTarefa(request):
    categorias = Categoria.objects.all()
    tarefas = Tarefa.objects.all()
    sede = DadosSede.objects.all()

    dicionario = {
        "lista_categorias": categorias,
        "lista_tarefas" : tarefas,
        "info_sede": sede[0]
    }
    return render(request, "relatorioTarefa.html", dicionario)
