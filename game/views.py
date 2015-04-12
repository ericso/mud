from django.shortcuts import render
from django.http import JsonResponse
# from django.core import serializers

from game.models import WorldNode


def node(request):
  """
  """
  node = WorldNode.objects.get(
    x_pos=request.GET.get('x', None),
    y_pos=request.GET.get('y', None)
  )
  node_dict = {
    'x': node.x_pos,
    'y': node.y_pos,
    'text': node.text,
  }

  data = {
    'node': node_dict
  }

  return JsonResponse(data)
