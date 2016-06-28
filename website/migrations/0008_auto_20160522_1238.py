# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20160522_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receitas',
            name='tempo_de_preparo',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
