# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_nodetext'),
    ]

    operations = [
        migrations.AddField(
            model_name='dungeon',
            name='name',
            field=models.TextField(default=b'Dungeon'),
            preserve_default=True,
        ),
    ]
