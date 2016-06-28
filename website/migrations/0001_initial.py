# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=20, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriasMacro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=20, unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=20, null=True)),
                ('quantidade', models.FloatField(null=True)),
                ('unidade_de_medida', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('data_de_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('modo_de_preparo', models.TextField()),
                ('tempo_de_preparo', models.TimeField()),
                ('rendimento', models.PositiveIntegerField(null=True)),
                ('grau_de_dificuldade', models.PositiveIntegerField()),
                ('imagem', models.ImageField(upload_to='fotos', null=True)),
                ('categorias', models.ManyToManyField(to='website.Categorias')),
                ('ingredientes', models.ManyToManyField(to='website.Ingredientes')),
            ],
        ),
        migrations.AddField(
            model_name='categorias',
            name='categoria_macro',
            field=models.ForeignKey(to='website.CategoriasMacro'),
        ),
    ]
