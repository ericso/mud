import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from game.models import WorldNode


def dungeon(request, dungeon_id=None):
  """
  """
  return HttpResponse()
