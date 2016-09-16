# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soul', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='config',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='Config',
        ),
    ]
