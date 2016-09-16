# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, db_index=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(unique=True, max_length=50, db_index=True)),
                ('value', models.CharField(max_length=200, null=True)),
                ('created_by', models.ForeignKey(related_name='config_created_by', default=None, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='config_updated_by', default=None, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'config_config',
            },
        ),
    ]
