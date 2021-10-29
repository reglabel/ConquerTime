from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.

def tarefa_create(request):
    form = TarefaForm()
    if(request.method == 'POST'):
        form = TarefaForm(request.POST)
        if(form.is_valid()):
            form_nome_tarefa = form.cleaned_data['nome_tarefa']
            form_categoria = form.cleaned_data['categoria']
            form_insignia = form.cleaned_data['insignia']
            #form_duracao = form.cleaned_data['duracao']
            form_periodicidade = form.cleaned_data['periodicidade']
            form_frequencia_semana = form.cleaned_data['frequencia_semana']
            #form_data_e_hora_criacao = form.changed_data['data_e_hora_criacao']
            form_descricao = form.cleaned_data['descricao']
            #new_tarefa = Tarefa(nome_tarefa = form_nome_tarefa, categoria=form_categoria, insignia = form_insignia, duracao = form_duracao, periodicidade = form_periodicidade, frequencia_semana=form_frequencia_semana, data_e_hora_criacao = form_data_e_hora_criacao, descricao = form_descricao)
            new_tarefa = Tarefa(nome_tarefa = form_nome_tarefa, categoria=form_categoria, insignia = form_insignia, periodicidade = form_periodicidade, frequencia_semana=form_frequencia_semana, descricao = form_descricao)
            new_tarefa.save()
            return redirect('cronometro')

    elif(request.method == 'GET'):
        return render(request, 'add_tarefa.html', {'form': form})
    
    return render(request, 'add_tarefa.html', {'form': form})


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


def cronometro(request):
    categorias = Categoria.objects.all()
    tarefas = Tarefa.objects.all()
    sede = DadosSede.objects.all()

    dicionario = {
        "lista_categorias": categorias,
        "lista_tarefas" : tarefas,
        "info_sede": sede[0]
    }
    return render(request, "cronometro.html", dicionario)


def novaTarefa(request):
    categorias = Categoria.objects.all()
    tarefas = Tarefa.objects.all()
    sede = DadosSede.objects.all()

    dicionario = {
        "lista_categorias": categorias,
        "lista_tarefas" : tarefas,
        "info_sede": sede[0]
    }
    return render(request, "novaTarefa.html", dicionario)

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
