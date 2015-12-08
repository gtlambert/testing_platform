# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0028_auto_20151208_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productarticletest',
            old_name='parent_test_product',
            new_name='product_content_test',
        ),
    ]
