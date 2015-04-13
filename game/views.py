import json

from django.shortcuts import render
from django.http import JsonResponse, Http404
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
  data = {
    'status': None,
    'payload': None
  }

  if request.method == 'GET':
    if node_id:
      try:
        node = WorldNode.objects.get(pk=node_id)
      except:
        print("error")
        data['status'] = 'Error'
        raise Http404("Node could not be retrieved: %s" % (node_id,))
      else:
        data['status'] = 'Success'
        data['payload'] = serializers.serialize('json', [node])
        return JsonResponse(data)

    else:
      try:
        nodes = WorldNode.objects.all()
      except:
        data['status'] = 'Error'
        raise Http404("Node could not be retrieved: %s" % (node_id,))
      else:
        data['status'] = 'Success'
        data['payload'] = serializers.serialize('json', nodes)
        return JsonResponse(data)

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
      data['status'] = 'Error'
      raise Http404("Node could not be created")
    else:
      data['status'] = 'Success'
      data['payload'] = serializers.serialize('json', [node])
      return JsonResponse(data)

  elif request.method == 'PUT':
    params = json.loads(request.body)
    x = params.get('x', None)
    y = params.get('y', None)
    text = params.get('text', None)

    # Get the node
    try:
      node = WorldNode.objects.get(pk=node_id)
    except:
      data['status'] = 'Error'
      raise Http404("Node could not be found")
    else:
      # Update the node
      node.x = x
      node.y = y
      node.text = text

      try:
        node.save()
      except:
        data['status'] = 'Error'
        raise Http404("Node could not be updated")
      else:
        data['status'] = 'Success'
        data['payload'] = serializers.serialize('json', [node])
        return JsonResponse(data)
