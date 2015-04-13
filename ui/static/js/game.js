$(function() {

  // Setup the 'enter' keypress event
  $('input').keyup(function(e){
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

});
