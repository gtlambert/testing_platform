# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0014_auto_20151126_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingmismatchtest',
            name='content_type',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
