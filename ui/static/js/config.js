$(function() {
  'use strict';

  // Set up a global CSRF token for all AJAX calls
  // var CSRF_TOKEN = document.getElementById('csrf_token').value;
  $.ajaxSetup({
    headers: { 'X-CSRFToken': CSRF_TOKEN }
  });

  // Set up the 'enter' keypress event
  $('input').keyup(function(e) {
    if (e.keyCode == 13) {
      $(this).trigger('enter');
    }
  });

  $(document).ready(function(e) {
    $("body").css("paddingBottom", $("#id-console-in").height() + 10);
    $("#id-console-in").focus();
  });

  // Create a game object
  // The game object will hold all objects related to the game, such as
  //  world nodes, players, et.c
  app.game = app.game || {};
  app.gameCommands = app.gameCommands || {};
});
