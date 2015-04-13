from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
  url(r'^node/(?P<node_id>[0-9]+)/$', views.node, name='node'),
  url(r'^node/$', views.node, name='node'),
)
