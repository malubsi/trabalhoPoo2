# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20160520_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientes',
            name='unidade_de_medida',
            field=models.CharField(null=True, max_length=15),
        ),
        migrations.DeleteModel(
            name='Medidas',
        ),
    ]
