import json
import random

from django.test import TestCase, TransactionTestCase

from game.models import Dungeon, WorldNode


class GameTest(TestCase):
  """Test class for Game API
  Routes:
  GET /game/node/:dungeon/:id - Returns all nodes or a single one with :id from :dungeon
  POST /game/node/:dungeon - Adds a new node to :dungeon
  PUT /game/node/:id - Updates node
  DELETE /game/node/:id - Deletes the node with :id


  GET /game/dungeon/ - Returns JSON list of dungeons
  GET /game/dungeon/:id - Returns nodes for dungeon with :id
  """

  def setUp(self):
    """
    """
    self.api_endpoint_base = '/game/dungeon/'

  def tearDown(self):
    """
    """
    self._destroy_dungeons()

  def _create_dungeons(self):
    """Creates a Dungeon and its WorldNodes db records
    Returns the primary key of the dungeon
    """
    d1 = Dungeon.objects.create(
      name="World",
      description="This is the world!"
    )
    wn1 = WorldNode.objects.create(
      x = 0,
      y = 0,
      unvisited = 'Unvisited node 1',
      visited = 'Visited node 1',
      look = 'look node 1',
      dungeon = d1
    )
    wn2 = WorldNode.objects.create(
      x = 1,
      y = 0,
      unvisited = 'Unvisited node 2',
      visited = 'Visited node 2',
      look = 'look node 2',
      dungeon = d1
    )
    return d1.pk

  def _destroy_dungeons(self):
    """Deletes the Dungeon database
    """
    Dungeon.objects.all().delete()

  def _get_dungeons(self):
    """Send a GET request to the API endpoint /game/dungeon/
    Returns the response
    Expect response to be JSON containing all Dungeon info
    """
    path = self.api_endpoint_base
    response = self.client.get(
      path=path,
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    return response

  def _get_dungeon_nodes(self, dungeon_id):
    """Send a GET request to the API endpoint /game/dungeon/:id
    Returns the response
    Expect response to be JSON Dungeon info and nodes for the dungeon
     with :id
    """
    path = self.api_endpoint_base + str(dungeon_id)
    response = self.client.get(
      path=path,
      HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    return response


  ### Test Methods ###

  # GET
  def test_get_dungeon_returns_200(self):
    response = self._get_dungeons()
    self.assertEqual(response.status_code, 200)

  def test_get_dungeon_returns_status_success(self):
    self._create_dungeons()

    response = self._get_dungeons()
    resp_obj = json.loads(response.content.decode())
    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'success')



  def test_get_dungeon_retuns_list_of_dungeons(self):
    self._create_dungeons()

    response = self._get_dungeons()
    resp_obj = json.loads(response.content.decode())
    self.assertIn('data', resp_obj.keys())
    self.assertIn('dungeons', resp_obj['data'].keys())

    dungeons_obj = json.loads(resp_obj['data']['dungeons'])
    self.assertEqual(1, len(dungeons_obj))

  def test_get_dungeon_with_id_returns_single_dungeon(self):
    # TODO(eso) can I mock out the database
    # and get rid of this db transaction?
    dungeon_id = self._create_dungeons()

    response = self._get_dungeon_nodes(dungeon_id=dungeon_id)
    resp_obj = json.loads(response.content.decode())

    self.assertIn('data', resp_obj.keys())
    self.assertIn('dungeons', resp_obj['data'].keys())

  def test_get_dungeon_with_incorrect_id_returns_error_status(self):
    dungeon_id = self._create_dungeons()
    print(dungeon_id)

    # Get a random integer to test incorrect dungeon id
    rand_id = random.randint(1, 1000)
    while dungeon_id == rand_id:
      rand_id = random.randint(1, 1000)

    response = self._get_dungeon_nodes(dungeon_id=rand_id)
    resp_obj = json.loads(response.content.decode())

    self.assertIn('status', resp_obj.keys())
    self.assertEqual(resp_obj['status'], 'fail')
    self.assertEqual(resp_obj['message'], 'dungeon with id: %s does not exist' % (rand_id,))
