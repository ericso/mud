import json

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from game.models import WorldNode


def node(request, node_id=None):
  """
  Routes:
  GET /game/node/:id - Returns all nodes or a single one with :id
  POST /game/node/ - Adds a new node
  PUT /game/node/:id - Updates node
  DELETE /game/node/:id - Deletes the node with :id
  """
  response = {}

  if request.method == 'GET':
    if node_id:
      try:
        node = WorldNode.objects.get(pk=node_id)
      except:
        # Should somehow return a 404 error message
        # TODO(eso) use Django REST Framework
        response['status'] = "fail"
        response['message'] = "node with id: %s does not exist" % (node_id,)
      else:
        response['status'] = "success"
        response['data'] = {}
        response['data']['nodes'] = serializers.serialize('json', [node])
      finally:
        return JsonResponse(response)

    else:
      try:
        nodes = WorldNode.objects.all()
      except:
        response['status'] = "error"
        response['message'] = 'could not retrieve nodes'
      else:
        response['status'] = "success"
        response['data'] = {}
        response['data']['nodes'] = serializers.serialize('json', nodes)
      finally:
        return JsonResponse(response)

  elif request.method == 'POST':
    # Parameters are in the request body, since POST type is
    #  `application/json`
    params = json.loads(request.body)
    x = params.get('x', None)
    y = params.get('y', None)
    text = params.get('text', None)

    try:
      node = WorldNode.objects.create(x=x, y=y, text=text)
    except:
      response['status'] = "fail"
      response['message'] = 'could not create node'
    else:
      response['status'] = "success"
      response['data'] = {}
      response['data']['nodes'] = serializers.serialize('json', [node])
    finally:
      return JsonResponse(response)

  elif request.method == 'PUT':
    params = json.loads(request.body)
    x = params.get('x', None)
    y = params.get('y', None)
    text = params.get('text', None)

    # Get the node
    try:
      node = WorldNode.objects.get(pk=node_id)
    except:
      response['status'] = "fail"
      response['message'] = "could not get node to update"
    else:
      # Update the node
      node.x = x
      node.y = y
      node.text = text

      try:
        node.save()
      except:
        response['status'] = 'fail'
        response['message'] = 'node with id: %s could not be updated' % (node_id,)
        # TODO(eso) write test for this branch
      else:
        response['status'] = 'success'
        response['data'] = {}
        response['data']['nodes'] = serializers.serialize('json', [node])

    finally:
      return JsonResponse(response)

  elif request.method == 'DELETE':
    # Delete the node
    try:
      WorldNode.objects.get(pk=node_id).delete()
    except:
      response['status'] = 'fail'
      response['message'] = "node could not be deleted"
    else:
      response['status'] = 'success'
    finally:
      return JsonResponse(response)
