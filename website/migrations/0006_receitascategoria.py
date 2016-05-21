# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20160521_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceitasCategoria',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('categoria_macro', models.ManyToManyField(to='website.CategoriasMacro')),
                ('categorias', models.ManyToManyField(to='website.Categorias')),
                ('receitas', models.ManyToManyField(to='website.Receitas')),
            ],
        ),
    ]
