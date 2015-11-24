# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0005_auto_20151124_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='datetime_started',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 24, 15, 54, 42, 610000)),
        ),
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='num_products_tested',
            field=models.IntegerField(default=0),
        ),
    ]
