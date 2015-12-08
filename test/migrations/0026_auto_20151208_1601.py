# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0025_auto_20151208_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcontenttest',
            name='content_type',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='productcontenttest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 16, 0, 56, 716000), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcontenttest',
            name='datetime_finished',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='productcontenttest',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productcontenttest',
            name='num_products',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcontenttest',
            name='num_products_tested',
            field=models.IntegerField(default=0),
        ),
    ]
