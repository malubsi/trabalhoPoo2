# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160520_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='unidade_de_medida',
            field=models.ForeignKey(to='website.Medidas'),
        ),
    ]
