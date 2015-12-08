# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0020_auto_20151208_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenttestproduct',
            name='content_url',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
