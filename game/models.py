from django.db import models

class WorldNode(models.Model):
  """Represents a node in the game world
  """
  x = models.IntegerField()
  y = models.IntegerField()
  text = models.TextField()
