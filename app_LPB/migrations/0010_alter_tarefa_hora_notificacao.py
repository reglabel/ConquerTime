# Generated by Django 3.2.8 on 2021-10-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_LPB', '0009_auto_20211029_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='hora_notificacao',
            field=models.TimeField(null=True),
        ),
    ]
