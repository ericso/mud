from django.db import models

class WorldNode(models.Model):
  """Represents a node in the game world
  """
  x = models.IntegerField()
  y = models.IntegerField()


class Dungeon(models.Model):
  """Collection of nodes representing a place in the game.
  e.g. the world is a dungeon as is a house in the world, or a cave
  """
  name = models.TextField(default="Dungeon")
  description = models.TextField()
  location = models.ForeignKey(WorldNode)


class NodeText(models.Model):
  """Text that a player would see upon visiting a node
  """
  unvisited = models.TextField()
  visited = models.TextField()
  look = models.TextField()
  location = models.ForeignKey(WorldNode)
