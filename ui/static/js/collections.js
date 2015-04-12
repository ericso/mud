$(function() {
  'use strict';

  App.Collections.Nodes = Backbone.Collection.extend({
    url: function() {
      return  '/locations/'
    }
  });

});
