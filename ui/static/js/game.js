(function($) {

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

  function processCommand() {
    var inField = $("#in");
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

  function doStuff(args) {
    outputToConsole("I'll just echo the args: " + args);
  }

  function outputToConsole(text) {
    var p = $("<p>" + text + "</p>");
    $("#out").append(p);
    p.scrollIntoView();
  }

  $(document).ready(function(e) {
    $("body").css("paddingBottom", $("#in").get("offsetHeight"));
    $("#in").on("keydown", function(e) {
      if (e.keyCode === 13) {
        processCommand();
      }
    });
  });

})(jQuery);
