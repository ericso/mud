# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def populate_world(apps, schema_editor):
  """Creates WorldNode objects from
  """
  # world is a set of tuples representing nodes: (x, y, text)
  world = [
    (0, 0, "You wake up in a forest. Looking around, you see something north"),
    (0, 1, "More forest"),
    (0, 2, "You reach a high, smooth wall. The wall seems impenetrable and you are unable to get a foothold to climb."),
    (1, 0, "There is a river in the distance to the east."),
    (2, 0, "A wide rushing river is before you. The water is frigid. You see what seem to be angry beasts lurking below the surface. Strange eyes seem to appear in the woods across the river, but you can't be sure..."),
    (-1, 0, "To the west, you see a clearing with sun shine."),
    (-2, 0, "You come upon a clearing. In the clearing is a large stone with an engraving. You cannot read it for it is in a language you are unfamiliar with."),
    (0, -1, "To the south, is more forest, but you feel like something important is drawing you in that direction."),
    (0, -2, "A hut appears ahead. There is smoke billowing out of the chimney; a sign someone is home. You should probably knock on the door."),
  ]

  WorldNode = apps.get_model('game', 'WorldNode')
  for x, y, text in world:
    WorldNode.objects.create(x=x, y=y, text=text)


class Migration(migrations.Migration):

    dependencies = [
      ('game', '0002_auto_20150413_2144'),
    ]

    operations = [
      migrations.RunPython(populate_world)
    ]
