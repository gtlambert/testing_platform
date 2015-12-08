# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0019_articletestproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenttestproduct',
            name='brand',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='contenttestproduct',
            name='model',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
