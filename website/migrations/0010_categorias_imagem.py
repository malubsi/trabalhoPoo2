# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20160522_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorias',
            name='imagem',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]
