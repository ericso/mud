import json

from django.test import TestCase


class GameTest(TestCase):
  """Test class for Game API
  Routes:
  GET /nodes/x/y/ - Returns JSON containing game world nodes
  """

  def setUp(self):
    """Create a test question and associated answer in the database
    """
    pass


  def tearDown(self):
    """Clear test database
    """
    pass


  def _get_nodes(self, x=None, y=None, **kwargs):
    path = '/nodes/'
    if x:
      path += '%s/' % (x,)
    if y:
      path += '%s/' % (y,)

    response = self.client.put(
      path=path,
      data=kwargs,
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    return json.loads(response.content.decode())


  ### Test Methods ###
  # def test_get_nodes_returns_200(self):
  #   response = self.client.get(
  #     '/nodes/',
  #     HTTP_X_REQUESTED_WITH='XMLHttpRequest'
  #   )
  #   self.assertEqual(response.status_code, 200)

  # def test_get_nodes_returns_nodes_JSON(self):
  #   data = self._get_nodes()
  #   self.assertIn('question', data.keys())
