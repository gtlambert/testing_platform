# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0013_mismatchtestproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='mismatchtestproduct',
            name='tab_number_reviewers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mismatchtestproduct',
            name='tab_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mismatchtestproduct',
            name='widget_number_reviewers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mismatchtestproduct',
            name='widget_rating',
            field=models.IntegerField(default=0),
        ),
    ]
