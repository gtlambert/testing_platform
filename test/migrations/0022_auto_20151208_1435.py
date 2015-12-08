# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0021_contenttestproduct_content_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenttestproduct',
            name='number_reviews',
            field=models.IntegerField(default=-1, blank=True),
        ),
        migrations.AddField(
            model_name='contenttestproduct',
            name='rating',
            field=models.IntegerField(default=-1, blank=True),
        ),
    ]
