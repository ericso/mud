$(function() {
  'use strict';

  // Backbone View for console input
  App.Views.ConsoleInput = Backbone.View.extend({
    el: '#id-console-in',
    initialize: function() {
      this.render();
    },
    // render: function() {
    //   var that = this;
    // },
    events: {
      'enter': 'processCommand'
    },
    processCommand: function(event) {
      var inField = $("#id-console-in");
      var input = inField.val();
      var parts = input.replace(/\s+/g, " ").split(" ");
      var command = parts[0];
      var args = parts.length > 1 ? parts.slice(1, parts.length) : [];
      inField.val("");
      for (var i = 0; i < app.commands.length; i++) {
        if (command === app.commands[i].name) {
          app.commands[i].handler(args);
          return;
        }
      }
      app.outputToConsole("Unsupported Command: " + command);
    }

  });

  // Backbone View for console output
  App.Views.ConsoleOutput = Backbone.View.extend({
    el: '#id-console-out',
    // render: function() {
    //   var that = this;
    // }
  });

});
