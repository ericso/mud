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

      inField.val(""); // reset the input fields

      // Determine what the command is by doing a reverse look-up on
      //  command mapping dictionary
      var parsedCmd = _.findKey(app.gameCommands.mappings, function(lst) {
        return _.contains(lst, command);
      });

      for (var i=0; i<app.gameCommands.handlers.length; i++) {
        if (parsedCmd === app.gameCommands.handlers[i].name) {
          app.gameCommands.handlers[i].handler(args);
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
