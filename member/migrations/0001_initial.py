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
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('email', models.CharField(unique=True, max_length=100)),
                ('contact_number', models.CharField(unique=True, max_length=15)),
                ('password', models.CharField(default=None, max_length=128)),
                ('first_name', models.CharField(default=None, max_length=20)),
                ('last_name', models.CharField(default=None, max_length=20)),
                ('middle_name', models.CharField(default=None, max_length=20)),
                ('dob', models.DateField(default=None)),
                ('gender', models.CharField(default=None, max_length=10, choices=[(b'', b'Select'), (b'male', b'Male'), (b'female', b'Female')])),
                ('marital_status', models.CharField(default=None, max_length=10, choices=[(b'', b'Select'), (b'self', b'Self'), (b'son', b'Son'), (b'daughter', b'Daughter'), (b'brother', b'Brother'), (b'sister', b'Sister'), (b'relative', b'Relative')])),
                ('profile_creating_for', models.CharField(default=None, max_length=10, choices=[(b'', b'Select'), (b'unmarried', b'Unmarried'), (b'widow_or_widower', b'Widow or Widower'), (b'divorcee', b'Divorcee')])),
                ('created_by', models.ForeignKey(related_name='user_created_by', default=None, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='user_updated_by', default=None, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
