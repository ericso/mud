$(function() {

  app.testModels = function() {
    var nodeDetails = {
      x: 2,
      y: 2,
      text: "This is the node at 2,2"
    };
    app.node = new App.Models.WorldNode();

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
  };

  app.testCollections = function() {
    app.nodeCollection = new App.Collections.WorldNodes([], {
      // model: App.Models.WorldNode
    });
    console.log("created a node collection");

    app.nodeCollection.fetch().done(function(response) {
      console.log("fetched a node collection");
      console.log(response);

      app.nodeCollection.each(function(list, iterator, ctx) {
        console.log(list);
      });
    });

  }
});
