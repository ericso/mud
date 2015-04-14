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
  var node = new App.Models.NodeModel();

  // The server should save the data and return a response containing the new `id`
  console.log("about to save a node");
  node.save(nodeDetails, {
    success: function (n) {
      console.log(n);
      var id_ = JSON.parse(n.get('payload')['pk']);
      console.log(id_);
      console.log(n.toJSON());
    }
  });

  console.log(node);

  // node.save({
  //   id: 22,
  //   x: 5,
  //   y: 6,
  //   text: "This how we do it!",
  // });

  // console.log(node);

  // node.destroy();

  // console.log(node);

});
