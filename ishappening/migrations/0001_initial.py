# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('timestamp_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('title', models.TextField()),
                ('picture_url', models.URLField(max_length=600, blank=True)),
                ('html', models.TextField()),
                ('snippet', models.TextField()),
                ('approx_traffic', models.PositiveIntegerField()),
                ('country_id', models.PositiveIntegerField(db_index=True)),
                ('published', models.DateTimeField()),
                ('internal_url', models.URLField(unique=True, max_length=600, db_index=True)),
                ('external_url', models.URLField(unique=True, max_length=600, db_index=True)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]
