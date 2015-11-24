# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_auto_20151124_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='datetime_finished',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='review_rating_matches',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='review_rating_mismatches',
            field=models.IntegerField(default=0),
        ),
    ]
