# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedContentTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExportedContentTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='RatingMismatchTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_products', models.IntegerField()),
                ('num_products_tested', models.IntegerField()),
                ('datetime_started', models.DateTimeField(auto_now_add=True)),
                ('datetime_finished', models.DateTimeField(blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('review_number_matches', models.IntegerField(default=0)),
                ('review_number_mismatches', models.IntegerField(default=0)),
                ('review_rating_matches', models.IntegerField()),
                ('review_rating_mismatches', models.IntegerField()),
            ],
        ),
    ]
