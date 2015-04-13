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
    """
    """
    self.api_endpoint_base = '/game/node/'

  def tearDown(self):
    """
    """
    pass

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

  def _post_node(self, **kwargs):
    path = self.api_endpoint_base
    response = self.client.post(
      path=path,
      data=json.dumps(kwargs),
      content_type='application/json'
    )
    return response

  def _put_node(self, node_id, **kwargs):
    path = self.api_endpoint_base
    if node_id:
      path += str(node_id) + '/'

    response = self.client.put(
      path=path,
      data=json.dumps(kwargs),
      content_type='application/json'
    )
    return response

  ### Test Methods ###

  # GET
  def test_get_nodes_returns_200(self):
    response = self._get_nodes()
    self.assertEqual(response.status_code, 200)

  def test_get_nodes_returns_nodes_JSON_status(self):
    response = self._get_nodes()
    data = json.loads(response.content.decode())
    self.assertIn('status', data.keys())
    self.assertEqual(data['status'], 'Success')

  def test_get_node_with_id_returns_JSON_payload(self):
    # TODO(eso) can I mock out the database
    # and get rid of this db transaction?
    WorldNode.objects.create(
      x=0,
      y=0,
      text="Start Here"
    )
    response = self._get_nodes(node_id=1)
    data = json.loads(response.content.decode())
    self.assertIn('payload', data.keys())

  # POST
  def test_post_node_returns_JSON_status(self):
    node_data = {
      'x': 1,
      'y': 1,
      'text': "This is the node at 1,1"
    }
    response = self._post_node(**node_data)
    data = json.loads(response.content.decode())
    self.assertIn('status', data.keys())
    self.assertEqual(data['status'], 'Success')

  def test_broken_post_node_returns_error_status_404(self):
    node_data = {
      'x': 1,
      'y': None,
      'text': "This is a broken node"
    }
    response = self._post_node(**node_data)
    # data = json.loads(response.content.decode())
    self.assertEqual(response.status_code, 404)
    # self.assertIn('status', data.keys())
    # self.assertEqual(data['status'], 'Error')

  # PUT
  def test_put_to_existing_node_updates_node_properly(self):
    node_data = {
      'x': 1,
      'y': 1,
      'text': "This is the node at 1, 1"
    }
    response = self._post_node(**node_data)
    data = json.loads(response.content.decode())
    payload = json.loads(data['payload'])
    id_ = payload[0]['pk']
    fields = payload[0]['fields']

    self.assertIn('status', data.keys())
    self.assertEqual(data['status'], 'Success')
    self.assertEqual(fields['x'], 1)
    self.assertEqual(fields['y'], 1)
    self.assertEqual(fields['text'], "This is the node at 1, 1")

    update_data = {
      'x': 2,
      'y': 3,
      'text': "This is an updated node, now at 2, 3"
    }
    response = self._put_node(node_id=id_, **update_data)
    data = json.loads(response.content.decode())
    payload = json.loads(data['payload'])
    fields = payload[0]['fields']

    self.assertIn('status', data.keys())
    self.assertEqual(data['status'], 'Success')
    self.assertEqual(fields['x'], 2)
    self.assertEqual(fields['y'], 3)
    self.assertEqual(fields['text'], "This is an updated node, now at 2, 3")

  def test_put_without_id_results_in_error(self):
    node_data = {
      'x': 1,
      'y': 1,
      'text': "This is the node at 1, 1"
    }
    response = self._put_node(node_id=None, **node_data)
    # data = json.loads(response.content.decode())
    self.assertEqual(response.status_code, 404)
    # self.assertIn('status', data.keys())
    # self.assertEqual(data['status'], 'Error')
