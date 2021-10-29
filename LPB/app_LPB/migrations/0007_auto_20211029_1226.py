# Generated by Django 3.2.8 on 2021-10-29 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_LPB', '0006_auto_20211027_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='frequencia_dias',
            new_name='periodicidade',
        ),
        migrations.AddField(
            model_name='medalha',
            name='insignia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_LPB.insignia'),
        ),
    ]