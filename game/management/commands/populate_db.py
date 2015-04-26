from django.core.management.base import BaseCommand

from game.models import Dungeon, WorldNode
from game.management.commands.content import world, nodes

class Command(BaseCommand):
  """Populates the Dungeon and WorldNode databases
  """

  def _populate_db(self):
    self._populate_test_data()


  def _populate_test_data(self):
    """Populates the database with data for testing
    """
    d_world = Dungeon.objects.create(**world)
    for node in nodes:
      node['dungeon'] = d_world
      WorldNode.objects.create(**node)


  def _populate_real_data(self):
    """Production data population
    """
    pass


  def handle(self, *args, **options):
    """handle() is run when the management command is run
    """
    self._populate_db()
