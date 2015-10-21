# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishappening', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='external_url',
            field=models.URLField(unique=True, max_length=1024, db_index=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='internal_url',
            field=models.URLField(unique=True, max_length=1024, db_index=True),
        ),
    ]
