$(function() {
  'use strict';

  App.Models.NodeModel = Backbone.Model.extend({
    urlRoot: '/game/node/',
    parse: function(response, xhr) {
      var nodes = JSON.parse(response.data.nodes)

      return {
        'id': nodes[0].pk,
        'text': nodes[0].fields.text,
        'x': nodes[0].fields.x,
        'y': nodes[0].fields.y,
      }
    }
  });

});
