from django.forms import ModelForm
from .models import Tarefa

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        #fields = ['nome_tarefa', 'categoria', 'insignia', 'duracao','periodicidade', 'frequencia_semana', 'data_e_hora_criacao', 'descricao']
        fields = ['nome_tarefa', 'categoria', 'insignia','periodicidade', 'frequencia_semana', 'descricao']
