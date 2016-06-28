# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='unidade_de_medida',
            field=models.ForeignKey(to='website.Medidas'),
        ),
        migrations.AlterUniqueTogether(
            name='ingredientes',
            unique_together=set([('nome', 'quantidade', 'unidade_de_medida')]),
        ),
    ]
