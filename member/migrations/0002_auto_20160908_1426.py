# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]
