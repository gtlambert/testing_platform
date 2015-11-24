# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0004_auto_20151124_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='datetime_started',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 11, 24, 15, 47, 4, 28000)),
        ),
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
