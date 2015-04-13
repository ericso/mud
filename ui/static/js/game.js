$(function() {

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
    $("body").css("paddingBottom", $("#id-console-in").get("offsetHeight"));
  });

  // Add Backbone views
  app.consoleInput = new App.Views.ConsoleInput();
  app.consoleOutput = new App.Views.ConsoleOutput();


  var nodeDetails = {
    x: 2,
    y: 2,
    text: "This is the node at 2,2"
  };
  var node = new App.Models.NodeModel(nodeDetails);

  // The server should save the data and return a response containing the new `id`
  node.save({
    success: function (n) {
      alert(n.toJSON());
    }
  })
});
