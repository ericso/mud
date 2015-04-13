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
  if request.method == 'GET':
    node_list = []
    # x = request.GET.get('x', None)
    # y = request.GET.get('y', None)
    # if x and y:
    #   node = WorldNode.objects.get(
    #     x_pos=x,
    #     y_pos=y
    #   )

    #   node_list.append({
    #     'x': node.x_pos,
    #     'y': node.y_pos,
    #     'text': node.text,
    #   })

    data = {
      'status': None,
      'payload': None
    }

    if node_id:
      try:
        node = WorldNode.objects.get(pk=node_id)
      except:
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

