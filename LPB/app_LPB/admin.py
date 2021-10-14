from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(DadosEmpresas)
class DadosEmpresasAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa', 'texto_sobre')

@admin.register(DadosSede)
class DadosSedeAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa', 'texto_sobre')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'descricao', 'preco_custo', 'preco_venda')

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome_pessoa', 'email', 'propaganda')

