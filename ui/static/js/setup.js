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

  app.outputToConsole = function(text) {
    var p = $("<p>" + text + "</p>");
    var elOut = $("#id-console-out");
    elOut.append(p);

    var pos = p.position();
    $(document.body).scrollTop(pos.top);
  }

  app.commands = [
    {
      name: "do_stuff",
      handler: doStuff
    }, {
      name: "greet",
      handler: function(args) {
        app.outputToConsole("Hello " + args[0] + ", welcome to Console.");
      }
    }
  ];

  function doStuff(args) {
    app.outputToConsole("I'll just echo the args: " + args);
  }

});
