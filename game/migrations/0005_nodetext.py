# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20150426_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unvisited', models.TextField()),
                ('visited', models.TextField()),
                ('look', models.TextField()),
                ('location', models.ForeignKey(to='game.WorldNode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
