# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='datetime_finished',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='num_products',
            field=models.IntegerField(blank=True),
        ),
    ]
