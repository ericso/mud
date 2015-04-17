import json

from django.test import TestCase, TransactionTestCase

from game.models import WorldNode


class GameTest(TransactionTestCase):
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
      path += str(node_id)

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
      path += str(node_id)

    response = self.client.put(
      path=path,
      data=json.dumps(kwargs),
      content_type='application/json'
    )
    return response

  def _delete_node(self, node_id):
    path = self.api_endpoint_base
    if node_id:
      path += str(node_id)

    response = self.client.delete(
      path=path,
      content_type='application/json'
    )
    return response

  ### Test Methods ###

  # GET
  def test_get_nodes_returns_200(self):
    response = self._get_nodes()
    self.assertEqual(response.status_code, 200)

  def test_get_nodes_returns_status_success(self):
    response = self._get_nodes()
    resp_obj = json.loads(response.content.decode())
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'success')

  def test_get_node_returns_list_of_nodes(self):
    WorldNode.objects.create(
      x=0,
      y=0,
      text="Start Here"
    )
    WorldNode.objects.create(
      x=1,
      y=1,
      text="Another node"
    )
    response = self._get_nodes()

    resp_obj = json.loads(response.content.decode())
    self.assertIn('data', resp_obj.keys())
    self.assertIn('nodes', resp_obj['data'].keys())

    nodes_obj = json.loads(resp_obj['data']['nodes'])
    self.assertEqual(2, len(nodes_obj))

  def test_get_node_with_id_returns_single_node(self):
    # TODO(eso) can I mock out the database
    # and get rid of this db transaction?
    node = WorldNode.objects.create(
      x=0,
      y=0,
      text="Start Here"
    )
    node_id = node.pk
    response = self._get_nodes(node_id=node_id)
    resp_obj = json.loads(response.content.decode())

    self.assertIn('data', resp_obj.keys())
    self.assertIn('nodes', resp_obj['data'].keys())

  def test_get_node_with_incorrect_id_returns_error_status(self):
    node_id = 1
    response = self._get_nodes(node_id=node_id)
    resp_obj = json.loads(response.content.decode())

    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'fail')
    self.assertEqual(resp_obj['message'], 'node with id: %s does not exist' % (node_id,))

  # POST
  def test_post_node_returns_success_status(self):
    node_data = {
      'x': 1,
      'y': 1,
      'text': "This is the node at 1,1"
    }
    response = self._post_node(**node_data)
    resp_obj = json.loads(response.content.decode())

    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'success')

  def test_broken_post_node_returns_error_status_and_message(self):
    node_data = {
      'x': 1,
      'y': None,
      'text': "This is a broken node"
    }
    response = self._post_node(**node_data)
    resp_obj = json.loads(response.content.decode())

    # self.assertEqual(response.status_code, 404)
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'fail')
    self.assertEqual(resp_obj['message'], 'could not create node')

  # PUT
  def test_put_to_existing_node_updates_node_properly(self):
    node_data = {
      'x': 1,
      'y': 1,
      'text': "This is the node at 1, 1"
    }
    response = self._post_node(**node_data)

    resp_obj = json.loads(response.content.decode())
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'success')

    nodes = json.loads(resp_obj['data']['nodes'])
    id_ = nodes[0]['pk']
    fields = nodes[0]['fields']
    self.assertEqual(fields['x'], 1)
    self.assertEqual(fields['y'], 1)
    self.assertEqual(fields['text'], "This is the node at 1, 1")

    update_data = {
      'x': 2,
      'y': 3,
      'text': "This is an updated node, now at 2, 3"
    }
    response = self._put_node(node_id=id_, **update_data)

    resp_obj = json.loads(response.content.decode())
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'success')

    nodes = json.loads(resp_obj['data']['nodes'])
    fields = nodes[0]['fields']
    self.assertEqual(fields['x'], 2)
    self.assertEqual(fields['y'], 3)
    self.assertEqual(fields['text'], "This is an updated node, now at 2, 3")

  def test_put_to_node_without_id_results_in_error(self):
    node_data = {
      'x': 1,
      'y': 1,
      'text': "This is the node at 1, 1"
    }
    response = self._put_node(node_id=None, **node_data)

    resp_obj = json.loads(response.content.decode())
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], "fail")
    self.assertEqual(resp_obj['message'], "could not get node to update")

  # # DELETE
  def test_delete_existing_node_removes_node_properly(self):
    # Add a node
    node_data = {
      'x': 1,
      'y': 1,
      'text': "This is the node at 1, 1"
    }
    response = self._post_node(**node_data)

    resp_obj = json.loads(response.content.decode())
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'success')

    nodes = json.loads(resp_obj['data']['nodes'])
    node_id = nodes[0]['pk']
    # fields = nodes[0]['fields']
    # self.assertEqual(fields['x'], 1)
    # self.assertEqual(fields['y'], 1)
    # self.assertEqual(fields['text'], "This is the node at 1, 1")

    # Delete that node
    response = self._delete_node(node_id=node_id)

    resp_obj = json.loads(response.content.decode())
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'success')

    # Make sure the node is gone
    response = self._get_nodes(node_id=node_id)

    resp_obj = json.loads(response.content.decode())
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'fail')
    self.assertEqual(resp_obj['message'], 'node with id: %s does not exist' % (node_id,))

  def test_delete_node_without_id_results_in_error(self):
    response = self._delete_node(node_id=None)

    resp_obj = json.loads(response.content.decode())
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'fail')
    self.assertEqual(resp_obj['message'], 'node could not be deleted')
