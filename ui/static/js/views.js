$(function() {
  'use strict';

  var COMMANDS = [
    {
      name: "do_stuff",
      handler: doStuff
    }, {
      name: "greet",
      handler: function(args) {
        outputToConsole("Hello " + args[0] + ", welcome to Console.");
      }
    }
  ];

  function doStuff(args) {
    outputToConsole("I'll just echo the args: " + args);
  }

  function outputToConsole(text) {
    var p = $("<p>" + text + "</p>");
    $("#id-console-out").append(p);
    p.scrollIntoView();
  }

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
      for (var i = 0; i < COMMANDS.length; i++) {
        if (command === COMMANDS[i].name) {
          COMMANDS[i].handler(args);
          return;
        }
      }
      outputToConsole("Unsupported Command: " + command);
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
