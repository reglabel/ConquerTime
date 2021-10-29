from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Categoria(models.Model):
    nome_categoria = models.CharField('Nome Categoria', max_length=250)
    descricao = models.TextField('Descricao')
    #falta inserir dps as estatisticas
    def __str__(self) -> str:
        return self.nome_categoria

class DadosSede(models.Model):
    nome_empresa = models.CharField('Nome da empresa', max_length=250)
    texto_sobre = models.TextField('Sobre nós')
    chamada = models.TextField('Chamada', null=True)
    whatsapp = models.TextField('Whatsapp', null=True, blank=True)
    localizacao = models.TextField('Localização', null=True, blank=True)
    instagram = models.TextField("Instagram", null=True, blank=True)
    email = models.TextField(null=True);

    def __str__(self) -> str:
        return self.nome_empresa

DIAS_CHOICES =(
    ("SE", "Segunda"),
    ("TE", "Terça"),
    ("QA", "Quarta"),
    ("QI", "Quinta"),
    ("SX", "Sexta"),
    ("SA", "Sabado"),
    ("DM", "Domingo"),
)

class Usuario(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Insignia(models.Model):
    nome_insignia = models.CharField(max_length=100)
    xp_maximo = models.IntegerField(default=500)
    lvl_maximo = models.IntegerField(default=10)
    lvl_atual = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.nome_insignia

class Medalha(models.Model):
    insignia = models.ForeignKey(Insignia, on_delete=models.CASCADE, null=True)
    nome_medalha = models.CharField(max_length=100)
    xp_atribuido = models.IntegerField(default=100)

class Tarefa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    insignia = models.ForeignKey(Insignia, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    nome_tarefa = models.CharField('Nome Tarefa', max_length=250)
    descricao = models.TextField('Descrição')
    #duracao = models.TimeField(null=True)
    hora_notificacao = models.TimeField(null=True)
    frequencia_semana = MultiSelectField(choices=DIAS_CHOICES, null=True)
    periodicidade = models.IntegerField(default=1)
    concluida = models.BooleanField(default=False)
    #data_e_hora_criacao = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.nome_tarefa
