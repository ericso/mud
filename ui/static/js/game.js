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
  app.node = new App.Models.NodeModel();

  console.log("about to create a node");
  app.node.save(
    nodeDetails
  ).done(function(data, textStatus, jqXHR) {
    console.log(data);

    var nodes = JSON.parse(data.data.nodes);
    var node_id = nodes[0].pk;
    console.log(node_id);
    console.log(app.node);

    console.log("about to update a node");
    app.node.save({
      id: app.node.id,
      x: 5,
      y: 6,
      text: "This how we do it!",
    }).done(function(data, textStatus, jqXHR) {
      console.log(data);

      console.log("about to destroy a node");
      app.node.destroy().done(function(data, textStatus, jqXHR) {
        console.log("done destroying a node");
        console.log(data);

        console.log("delete app.node from client");
        delete(app.node);
        console.log(app.node);
      });
    });
  });

});
