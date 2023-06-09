# Generated by Django 3.2.19 on 2023-05-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='horas_aulas',
            field=models.PositiveIntegerField(default=40),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='obrigatoria',
            field=models.BooleanField(default=True, verbose_name='Obrigatória'),
        ),
        migrations.AddField(
            model_name='turma',
            name='turno',
            field=models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite')], default=('manha', 'Manhã'), max_length=10),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='idade',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='turma',
            name='ano',
            field=models.PositiveIntegerField(),
        ),
    ]
