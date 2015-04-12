import json

from django.test import TestCase

from game.models import WorldNode


class GameTest(TestCase):
  """Test class for Game API
  Routes:
  GET /game/node/x/y/ - Returns JSON containing game world nodes
  """

  def setUp(self):
    """Create a test question and associated answer in the database
    """
    self.origin = WorldNode.objects.create(
      x_pos=0,
      y_pos=0,
      text="Start Here"
    )

  def tearDown(self):
    """Clear test database
    """
    WorldNode.objects.all().delete()


  def _get_nodes(self, x=None, y=None, **kwargs):
    path = '/game/node/'

    kwargs['x'] = x
    kwargs['y'] = y

    response = self.client.get(
      path=path,
      data=kwargs,
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    return response

  ### Test Methods ###
  def test_get_nodes_returns_200(self):
    response = self._get_nodes(0, 0)
    self.assertEqual(response.status_code, 200)

  def test_get_nodes_returns_nodes_JSON(self):
    response = self._get_nodes(0, 0)
    data = json.loads(response.content.decode())
    self.assertIn('node', data.keys())
