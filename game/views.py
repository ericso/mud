from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def node(request, x, y):

  data = {
    'node': 'node obj',
  }

  return JsonResponse(data)
