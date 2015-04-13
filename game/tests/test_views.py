import json

from django.test import TestCase

from game.models import WorldNode


class GameTest(TestCase):
  """Test class for Game API
  Routes:
  GET /game/node/:id - Returns all nodes or a single one with :id
  POST /game/node/ - Adds a new node
  PUT /game/node/:id - Updates node
  DELETE /game/node/:id - Deletes the node with :id
  """

  def setUp(self):
    """Create a test question and associated answer in the database
    """
    self.api_endpoint_base = '/game/node/'

    self.origin = WorldNode.objects.create(
      x_pos=0,
      y_pos=0,
      text="Start Here"
    )
    WorldNode.objects.create(
      x_pos=0,
      y_pos=1,
      text="Just north of origin"
    )

  def tearDown(self):
    """Clear test database
    """
    WorldNode.objects.all().delete()

  # def _get_nodes_with_coords(self, x=None, y=None, **kwargs):
  #   path = self.api_endpoint_base

  #   kwargs['x'] = x
  #   kwargs['y'] = y

  #   response = self.client.get(
  #     path=path,
  #     data=kwargs,
  #     HTTP_X_REQUESTED_WITH='XMLHttpRequest'
  #   )
  #   return response

  def _get_nodes(self, node_id=None, **kwargs):
    path = self.api_endpoint_base

    if node_id:
      path += str(node_id) + '/'

    response = self.client.get(
      path=path,
      data=kwargs,
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    return response

  ### Test Methods ###
  def test_get_nodes_returns_200(self):
    response = self._get_nodes()
    self.assertEqual(response.status_code, 200)

  def test_get_nodes_returns_nodes_JSON_status(self):
    response = self._get_nodes()
    data = json.loads(response.content.decode())
    self.assertIn('status', data.keys())
    self.assertEqual(data['status'], 'Success')

  def test_get_node_with_id_returns_JSON_payload(self):
    response = self._get_nodes(node_id=1)
    data = json.loads(response.content.decode())
    self.assertIn('payload', data.keys())
