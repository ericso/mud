from django.db import models

class WorldNode(models.Model):
  """Represents a node in the game world
  """
  x_pos = models.IntegerField()
  y_pos = models.IntegerField()
  text = models.TextField()
