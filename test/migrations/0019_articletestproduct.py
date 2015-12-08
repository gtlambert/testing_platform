# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0018_contenttestproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTestProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_id', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('parent_product', models.ForeignKey(to='test.ContentTestProduct')),
            ],
        ),
    ]
