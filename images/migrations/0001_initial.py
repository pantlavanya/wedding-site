# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import images.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, db_index=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('uses', models.CharField(db_index=True, max_length=50, null=True, choices=[(b'SLIDER_IMAGE', b'SLIDER IMAGE'), (b'PROFILE_IMAGE', b'PROFILE IMAGE'), (b'ADVERTISEMENT_IMAGE', b'ADVERTISEMENT IMAGE'), (b'OTHER_IMAGE', b'OTHER IMAGE')])),
                ('path', models.ImageField(max_length=500, null=True, verbose_name=b'Upload', upload_to=images.models.sort_files_by_extension)),
                ('original_name', models.CharField(max_length=200, null=True, editable=False)),
                ('modified_name', models.CharField(max_length=200, unique=True, null=True, editable=False, db_index=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('dimensions', models.CharField(max_length=50, null=True)),
                ('size', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('cron_checked', models.BooleanField(default=False)),
                ('cron_comment', models.TextField(null=True)),
                ('created_by', models.ForeignKey(related_name='images_created_by', default=None, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='images_updated_by', default=None, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'images_images',
            },
        ),
    ]
