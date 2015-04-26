from django.db import models


class Dungeon(models.Model):
  """Collection of nodes representing a place in the game.
  e.g. the world is a dungeon as is a house in the world, or a cave
  """
  name = models.TextField(default="Dungeon")
  description = models.TextField()


class WorldNode(models.Model):
  """Represents a node in the game world
  """
  x = models.IntegerField()
  y = models.IntegerField()
  unvisited = models.TextField()
  visited = models.TextField()
  look = models.TextField()
  dungeon = models.ForeignKey(Dungeon)

