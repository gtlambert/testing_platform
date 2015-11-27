# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0015_ratingmismatchtest_content_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_products', models.IntegerField(blank=True)),
                ('num_products_tested', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('datetime_finished', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('content_type', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='ExportedContentTest',
            new_name='ContentTestProduct',
        ),
        migrations.DeleteModel(
            name='ApprovedContentTest',
        ),
    ]
