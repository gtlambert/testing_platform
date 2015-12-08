# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0024_auto_20151208_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductArticleTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.CharField(max_length=30, blank=True)),
                ('article_id', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('article_url', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductContentTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.CharField(max_length=10)),
                ('content_url', models.CharField(max_length=300, blank=True)),
                ('brand', models.CharField(max_length=100, blank=True)),
                ('model', models.CharField(max_length=300, blank=True)),
                ('number_reviews', models.IntegerField(default=-1, blank=True)),
                ('rating', models.IntegerField(default=-1, blank=True)),
                ('article_ids', models.TextField(max_length=10000, blank=True)),
                ('overview_html', models.TextField(blank=True)),
                ('parent_test', models.ForeignKey(to='test.ContentTest')),
            ],
        ),
        migrations.RemoveField(
            model_name='articletestproduct',
            name='parent_test_product',
        ),
        migrations.RemoveField(
            model_name='contenttestproduct',
            name='parent_test',
        ),
        migrations.DeleteModel(
            name='ArticleTestProduct',
        ),
        migrations.DeleteModel(
            name='ContentTestProduct',
        ),
        migrations.AddField(
            model_name='productarticletest',
            name='parent_test_product',
            field=models.ForeignKey(to='test.ProductContentTest'),
        ),
    ]
