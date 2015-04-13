from django.shortcuts import render
from django.http import JsonResponse
# from django.core import serializers

from game.models import WorldNode


def node(request):
  """
  Routes:

  GET /game/node/ - Returns JSON containing game world nodes
  """
  x = request.GET.get('x', None)
  y = request.GET.get('y', None)

  node_list = []

  if x and y:
    node = WorldNode.objects.get(
      x_pos=x,
      y_pos=y
    )

    node_list.append({
      'x': node.x_pos,
      'y': node.y_pos,
      'text': node.text,
    })

  data = {
    'nodes': node_list
  }

  return JsonResponse(data)


# TODO(make node return a set of nodes, some distance from x, y)
