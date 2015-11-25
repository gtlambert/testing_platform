# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0008_auto_20151125_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratingmismatchtest',
            old_name='review_number_matches',
            new_name='number_reviewers_matches',
        ),
        migrations.RenameField(
            model_name='ratingmismatchtest',
            old_name='review_number_mismatches',
            new_name='number_reviewers_mismatches',
        ),
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='datetime_started',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 9, 58, 26, 426000)),
        ),
    ]
