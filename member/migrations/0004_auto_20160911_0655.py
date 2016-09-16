# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20160910_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='created_by',
            field=models.ForeignKey(related_name='member_created_by', default=None, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_by',
            field=models.ForeignKey(related_name='member_updated_by', default=None, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
