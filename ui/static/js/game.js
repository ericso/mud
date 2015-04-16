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

  // Create a player object
  app.player = {
    name: "Unknown Person",
    position: {
      x: 0,
      y: 0
    },
    updatePosition: function(x, y) {
      this.position.x = x;
      this.position.y = y;
    },
  }

  // TODO(eso) refactor function to print players curr pos text

  app.world = new App.Collections.WorldNodes();
  app.world.fetch().done(function(response) {
    var currPos = app.world.where({
      x: app.player.position.x,
      y: app.player.position.y,
    })[0];
    app.outputToConsole(currPos.get('text'));
  });

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

  // Game functions
  // These are executed based on what the player types
  app.move = function(args) {
    // Take the current user's position
    // move the user to the new position
    // call function to print out current position's text

    // app.outputToConsole("move() args: " + args);

    if (_.contains(args, 'north')) {
      // currPosY++;
      app.player.position.y++;
    } else if (_.contains(args, 'south')) {
      // currPosY--;
      app.player.position.y--;
    } else if (_.contains(args, 'east')) {
      // currPosX++;
      app.player.position.x++;
    } else if (_.contains(args, 'west')) {
      // currPosX--;
      app.player.position.x--;
    } else {
      app.outputToConsole("did not understand direction");
    }

    console.log(app.player.position);

    var currPos = app.world.where({
      x: app.player.position.x,
      y: app.player.position.y,
    })[0];

    app.outputToConsole(currPos.get('text'));

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
