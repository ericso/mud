$(function() {
  'use strict';

  App.Models.WorldNode = Backbone.Model.extend({
    urlRoot: '/game/node/',
    parse: function(response, xhr) {
      // Check to see if response is the raw JSON from server
      //  or parsed node array from collection parse()
      var nodes = null;
      if (_.isObject(response.data)) {
        // Fetch performed on model instance,
        //  returning array of a single node
        nodes = JSON.parse(response.data.nodes)[0];
      } else {
        // Fetch performed on collection
        nodes = response;
      }

      return {
        'id': nodes.pk,
        'text': nodes.fields.text,
        'x': nodes.fields.x,
        'y': nodes.fields.y,
      }
    }
  });

});
