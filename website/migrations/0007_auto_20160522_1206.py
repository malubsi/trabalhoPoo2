# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_receitascategoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receitascategoria',
            old_name='categoria_macro',
            new_name='macro',
        ),
    ]
