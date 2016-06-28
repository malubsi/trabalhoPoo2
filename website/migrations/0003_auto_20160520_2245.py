# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20160520_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientes',
            name='unidade_de_medida',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.DeleteModel(
            name='Medidas',
        ),
    ]
