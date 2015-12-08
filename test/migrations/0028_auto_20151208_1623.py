# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0027_auto_20151208_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='productarticletest',
            name='body_html',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='productarticletest',
            name='overview_html',
            field=models.TextField(blank=True),
        ),
    ]
