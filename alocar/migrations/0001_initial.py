# Generated by Django 2.2.5 on 2020-06-25 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloco', models.CharField(max_length=30, unique=True, verbose_name='Bloco')),
                ('criada', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado', models.DateTimeField(auto_now=True, verbose_name='Alterado')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(help_text='Ex= 00:00/00:00', max_length=23, unique=True, verbose_name='Horário')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('alterado', models.DateTimeField(auto_now=True, verbose_name='Alterado')),
            ],
            options={
                'verbose_name': 'Horário',
                'verbose_name_plural': 'Horários',
                'ordering': ['horario'],
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma', models.CharField(max_length=8, unique=True, verbose_name='Turma')),
                ('curso', models.CharField(max_length=50, verbose_name='Curso')),
                ('periodo', models.CharField(max_length=50, verbose_name='Periodo')),
                ('disciplina', models.CharField(max_length=50, verbose_name='Disciplina')),
                ('qtdalunos', models.PositiveSmallIntegerField(verbose_name='Qtd')),
                ('alocada', models.BooleanField(default=False, verbose_name='Alocada')),
                ('professor', models.CharField(max_length=50, verbose_name='Professor')),
                ('internet', models.BooleanField(default=False, verbose_name='Internet')),
                ('projetor', models.BooleanField(default=False, verbose_name='Projetor')),
                ('computador', models.BooleanField(default=False, verbose_name='Computador')),
                ('criada', models.DateTimeField(auto_now_add=True, verbose_name='Criada')),
                ('alterada', models.DateTimeField(auto_now=True, verbose_name='Alterada')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
                'ordering': ['curso', 'periodo'],
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(help_text='Descrição', max_length=50, unique=True, verbose_name='Sala')),
                ('capmaxima', models.PositiveSmallIntegerField(verbose_name='Cap. Máxima:')),
                ('disponivel', models.BooleanField(default=True, verbose_name='Disponivel')),
                ('internet', models.BooleanField(default=False, verbose_name='Internet')),
                ('projetor', models.BooleanField(default=True, verbose_name='Projetor')),
                ('computador', models.BooleanField(default=False, verbose_name='Computador')),
                ('criada', models.DateTimeField(auto_now_add=True, verbose_name='Criada')),
                ('alterada', models.DateTimeField(auto_now=True, verbose_name='Alterada ')),
                ('bloco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alocar.Bloco')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'ordering': ['sala'],
            },
        ),
        migrations.CreateModel(
            name='Alocar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criada', models.DateTimeField(auto_now_add=True, verbose_name='Criada')),
                ('alterada', models.DateTimeField(auto_now=True, verbose_name='Alterada')),
                ('dia', models.CharField(choices=[('Segunda', 'Segunda'), ('Terça', 'Terça'), ('Quarta', 'Quarta'), ('Quinta', 'Quinta'), ('Sexta', 'Sexta'), ('Sabado', 'Sabado')], max_length=11, verbose_name='Dia')),
                ('horario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='alocar.Horario')),
                ('sala', models.ForeignKey(limit_choices_to={'disponivel': True}, on_delete=django.db.models.deletion.PROTECT, to='alocar.Sala')),
                ('turma', models.ForeignKey(limit_choices_to={'alocada': False}, on_delete=django.db.models.deletion.PROTECT, related_name='alocar', to='alocar.Turma')),
            ],
            options={
                'verbose_name': 'Alocação',
                'verbose_name_plural': 'Alocações',
                'ordering': ['turma__curso', 'turma__periodo', 'turma__disciplina'],
            },
        ),
    ]
