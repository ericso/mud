from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
  url(r'^dungeon/(?P<dungeon_id>w+)$', views.dungeon, name='dungeon'),
  url(r'^dungeon/$', views.dungeon, name='dungeon'),
)
