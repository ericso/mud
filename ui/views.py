from django.shortcuts import render


def home(request):
  """Renders the home view of the app
  """
  return render(request, 'home.html')
