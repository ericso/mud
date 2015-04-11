from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mud.views.home', name='home'),
    url(r'^game/', include('game.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
