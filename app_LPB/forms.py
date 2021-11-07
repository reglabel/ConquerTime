from django.db.models.fields import DateField
from .models import Tarefa, Categoria
from django.forms import ModelForm, fields
from django.forms import TimeInput, DateInput, CheckboxSelectMultiple
from site_LPB.settings import DATE_INPUT_FORMATS, TIME_INPUT_FORMATS
from django import forms


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa

        #fields = [
        #    'nome_tarefa',
        #    'categoria',
        #    'insignia',
        #    'duracao',
        #    'periodicidade',
        #    'frequencia_semana',
        #    'data_criacao',
        #    'hora_criacao',
        #    'descricao',
        #    'hora_notificacao'
        #]

        #widgets = {
        #    'data_criacao': DateInput(attrs={'type':'date'},format=["%m/%d/%Y","%d/%m/%Y"]),
        #    'hora_criacao': TimeInput(attrs={'type':'time'},format=["%H:%M","%I:%M %p"]),
        #    'hora_notificacao': TimeInput(attrs={'type':'time'},format=["%H:%M","%I:%M %p"]),
        #    'frequencia_semana': CheckboxSelectMultiple(),
        #}

        fields = [
            'nome_tarefa',
            'categoria',
            'insignia',
            'duracao',
            'periodicidade',
            'frequencia_semana',
            'descricao',
        ]

        widgets = {
            'duracao': forms.Select(),
            'frequencia_semana': CheckboxSelectMultiple(),
        }

        #fields = ['nome_tarefa', 'categoria', 'insignia', 'periodicidade', 'frequencia_semana', 'descricao']


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome_categoria', 'descricao']

