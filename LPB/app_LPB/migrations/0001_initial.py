# Generated by Django 3.2.8 on 2021-10-13 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosEmpresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=250, verbose_name='Nome da empresa')),
                ('texto_sobre', models.TextField(verbose_name='Sobre nós')),
                ('whatsapp', models.TextField(blank=True, null=True, verbose_name='Whatsapp')),
                ('localizacao', models.TextField(blank=True, null=True, verbose_name='Localização')),
            ],
        ),
        migrations.CreateModel(
            name='DadosSede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=250, verbose_name='Nome da empresa')),
                ('texto_sobre', models.TextField(verbose_name='Sobre nós')),
                ('whatsapp', models.TextField(blank=True, null=True, verbose_name='Whatsapp')),
                ('localizacao', models.TextField(blank=True, null=True, verbose_name='Localização')),
                ('instagram', models.TextField(blank=True, null=True, verbose_name='Instagram')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=250, verbose_name='Nome do poduto')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('preco_custo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço de custo')),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço de venda')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_LPB.dadosempresas')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pessoa', models.CharField(max_length=50, verbose_name='Cliente')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('propaganda', models.BooleanField(verbose_name='Deseja receber ofertas?')),
                ('listagem', models.BooleanField(verbose_name='Deseja ser listado?')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_LPB.dadosempresas')),
            ],
        ),
    ]
