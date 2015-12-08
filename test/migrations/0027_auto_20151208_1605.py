# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0026_auto_20151208_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttest',
            name='num_products',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='productcontenttest',
            name='num_products',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='num_products',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
