$(function() {
  'use strict';

  App.Collections.WorldNodes = Backbone.Collection.extend({
    model: App.Models.WorldNode,
    url: '/game/node/',
    parse: function(response, xhr) {
      return JSON.parse(response.data.nodes);
    }
  });

});
