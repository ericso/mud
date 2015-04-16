$(function() {
  'use strict';

  // Setup console functionality
  app.outputToConsole = function(text) {
    var p = $("<p>" + text + "</p>");
    var elOut = $("#id-console-out");
    elOut.append(p);

    var pos = p.position();
    $(document.body).scrollTop(pos.top);
  }

  app.gameCommands.mappings = {
    'move': [
      'walk',
      'go',
      'move'
    ],
    'observe': [
      'look',
      'examine',
      'observe'
    ],
    'take': [
      'take',
      'get',
      'pick'
    ],
    'put': [
      'put',
      'place',
      'drop'
    ]
  }

  app.move = function(args) {
    app.outputToConsole("move() args: " + args);
  }
  app.observe = function(args) {
    app.outputToConsole("observe() args: " + args);
  }
  app.take = function(args) {
    app.outputToConsole("take() args: " + args);
  }
  app.put = function(args) {
    app.outputToConsole("put() args: " + args);
  }

  app.gameCommands.handlers = [
    {
      name: "move",
      handler: app.move
    }, {
      name: "observe",
      handler: app.observe
    }, {
      name: "take",
      handler: app.take
    }, {
      name: "put",
      handler: app.put
    },
  ];

  // Add Backbone views
  app.consoleInput = new App.Views.ConsoleInput();
  app.consoleOutput = new App.Views.ConsoleOutput();

  // Testing code
  // app.testModels();
  // app.testCollections();

});
