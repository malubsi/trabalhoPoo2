# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriasMacro',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=20, null=True)),
                ('categorias', models.ManyToManyField(to='malu_receitas.Categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, null=True)),
                ('quantidade', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(unique=True, max_length=20)),
                ('dataCriacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('modoPreparo', models.TextField()),
                ('tempoPreparo', models.TimeField()),
                ('rendimento', models.PositiveIntegerField(null=True)),
                ('grauDificuldade', models.PositiveIntegerField()),
                ('avaliacao', models.PositiveIntegerField(default=0, null=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='usuario')),
                ('categoria', models.ForeignKey(to='malu_receitas.Categorias', null=True)),
                ('ingredientes', models.ManyToManyField(to='malu_receitas.Ingredientes')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadesMedida',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(unique=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ingredientes',
            name='unidadeMedida',
            field=models.ManyToManyField(to='malu_receitas.UnidadesMedida'),
        ),
    ]
