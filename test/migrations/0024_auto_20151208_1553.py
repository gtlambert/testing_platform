# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0023_contenttestproduct_articles_ids'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articletestproduct',
            old_name='parent_product',
            new_name='parent_test_product',
        ),
        migrations.RenameField(
            model_name='contenttestproduct',
            old_name='articles_ids',
            new_name='article_ids',
        ),
        migrations.AddField(
            model_name='articletestproduct',
            name='article_url',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='articletestproduct',
            name='product_id',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='contenttestproduct',
            name='overview_html',
            field=models.TextField(blank=True),
        ),
    ]
