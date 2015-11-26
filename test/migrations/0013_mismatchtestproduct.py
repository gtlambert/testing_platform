# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0012_auto_20151125_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='MismatchTestProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.BooleanField(default=True)),
                ('product_id', models.CharField(max_length=10)),
                ('parent_test', models.ForeignKey(to='test.RatingMismatchTest')),
            ],
        ),
    ]
