from django.db import models

# Create your models here.

class DadosEmpresas(models.Model):
    nome_empresa = models.CharField('Nome da empresa', max_length=250)
    texto_sobre = models.TextField('Sobre nós')
    whatsapp = models.TextField('Whatsapp', null=True, blank=True)
    localizacao = models.TextField('Localização', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome_empresa

class DadosSede(models.Model):
    nome_empresa = models.CharField('Nome da empresa', max_length=250)
    texto_sobre = models.TextField('Sobre nós')
    chamada = models.TextField('Chamada', null=True)
    whatsapp = models.TextField('Whatsapp', null=True, blank=True)
    localizacao = models.TextField('Localização', null=True, blank=True)
    instagram = models.TextField("Instagram", null=True, blank=True)

    def __str__(self) -> str:
        return self.nome_empresa
    
class Produto(models.Model):
    empresa = models.ForeignKey(DadosEmpresas, on_delete=models.CASCADE, null=True)
    nome_produto = models.CharField('Nome do poduto', max_length=250)
    descricao = models.TextField('Descrição')
    preco_custo = models.DecimalField('Preço de custo', max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField('Preço de venda', max_digits=10, decimal_places=2)
 
class Pessoa(models.Model):
    empresa = models.ForeignKey(DadosEmpresas, on_delete=models.CASCADE, null=True)
    nome_pessoa = models.CharField('Cliente', max_length=50)
    email = models.EmailField("E-mail")
    propaganda = models.BooleanField("Deseja receber ofertas?")
    listagem = models.BooleanField("Deseja ser listado?")