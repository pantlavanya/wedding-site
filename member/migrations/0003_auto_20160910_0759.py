# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20160908_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'get_latest_by': 'created_at'},
        ),
        migrations.AlterField(
            model_name='member',
            name='contact_number',
            field=models.CharField(unique=True, max_length=15, db_index=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(unique=True, max_length=100, db_index=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='middle_name',
            field=models.CharField(default=None, max_length=20, verbose_name=b'Middle Name'),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(unique=True, max_length=50, db_index=True),
        ),
        migrations.AlterModelTable(
            name='member',
            table='member_member',
        ),
    ]
