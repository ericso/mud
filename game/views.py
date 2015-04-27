import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from game.models import Dungeon, WorldNode


def dungeon(request, dungeon_id=None):
  """
  Routes:
  GET /game/dungeon/ - Returns all dungeons
  GET /game/dungeon/:id - Returns all nodes of a dungeon with :id

  e.g.:
  response to GET /game/dungeon/
  {
    'status': 'success',
    'data': {
      'dungeons': [
        {
          'pk': dungeon_id,
          'name': 'dungeon name',
          'description': 'dungeon description',
        }
      ]
    }
  }

  response to GET /game/dungeon/:id
  {
    'status': 'success',
    'data': {
      'nodes': [
        'x': 0,
        'y': 1,
        'unvisited': 'some text',
        'visited': 'some other text',
        'look': 'and still more text',
      ]
    }
  }
  """
  response = {}

  if request.method == 'GET':
    if dungeon_id:
      try:
        dungeon = Dungeon.objects.get(pk=dungeon_id)
      except:
        # Should somehow return a 404 error message
        # TODO(eso) use Django REST Framework
        response['status'] = "fail"
        response['message'] = "dungeon with id: %s does not exist" % (dungeon_id,)
      else:
        response['status'] = "success"
        response['data'] = {}
        response['data']['dungeons'] = serializers.serialize('json', [dungeon])
      finally:
        return JsonResponse(response)
    else:
      try:
        dungeons = Dungeon.objects.all()
      except:
        response['status'] = "error"
        response['message'] = 'could not retrieve dungeons'
      else:
        response['status'] = "success"
        response['data'] = {}
        response['data']['dungeons'] = serializers.serialize('json', dungeons)
      finally:
        return JsonResponse(response)
