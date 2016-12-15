# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('range_field', models.CharField(max_length=200)),
                ('full_range_field', models.CharField(max_length=200)),
                ('char_field', models.CharField(max_length=230)),
            ],
        ),
    ]
