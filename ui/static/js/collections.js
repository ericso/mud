$(function() {
  'use strict';

  App.Collections.Nodes = Backbone.Collection.extend({
    model: Node,
    parse: function(response, xhr) {
      console.log("inside parse");
      console.log(response);
      console.log(xhr);
    }
  });

});
