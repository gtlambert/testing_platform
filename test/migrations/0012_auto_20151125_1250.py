# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0011_auto_20151125_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingmismatchtest',
            name='datetime_started',
        ),
        migrations.AddField(
            model_name='ratingmismatchtest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 12, 50, 40, 704000), auto_now_add=True),
            preserve_default=False,
        ),
    ]
