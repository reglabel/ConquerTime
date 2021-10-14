# Generated by Django 3.2.8 on 2021-10-14 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_LPB', '0002_dadossede_chamada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=250, verbose_name='Nome Categoria')),
                ('descricao', models.TextField(verbose_name='Descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Insignia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_insignia', models.CharField(max_length=100)),
                ('xp_maximo', models.IntegerField(default=500)),
                ('lvl_maximo', models.IntegerField(default=10)),
                ('lvl_atual', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Medalha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_medalha', models.CharField(max_length=100)),
                ('xp_atribuido', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tarefa', models.CharField(max_length=250, verbose_name='Nome Tarefa')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('duracao', models.TimeField()),
                ('hora_notificacao', models.TimeField()),
                ('hora_criacao', models.DateTimeField()),
                ('frequencia_dias', models.IntegerField(default=1)),
                ('concluida', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_LPB.categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='empresa',
        ),
        migrations.DeleteModel(
            name='DadosEmpresas',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]