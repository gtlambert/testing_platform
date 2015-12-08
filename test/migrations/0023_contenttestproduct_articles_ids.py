# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0022_auto_20151208_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenttestproduct',
            name='articles_ids',
            field=models.TextField(max_length=10000, blank=True),
        ),
    ]
