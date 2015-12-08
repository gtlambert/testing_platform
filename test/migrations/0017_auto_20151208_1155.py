# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0016_auto_20151127_0844'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContentTestProduct',
        ),
        migrations.AddField(
            model_name='contenttest',
            name='external_links_test',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
