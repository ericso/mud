# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worldnode',
            old_name='x_pos',
            new_name='x',
        ),
        migrations.RenameField(
            model_name='worldnode',
            old_name='y_pos',
            new_name='y',
        ),
    ]
