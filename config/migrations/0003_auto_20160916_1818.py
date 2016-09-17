# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20160911_0749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='config',
            old_name='name',
            new_name='key',
        ),
    ]
