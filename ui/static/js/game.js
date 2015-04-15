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

  // app.testModels();
  app.testCollections();

});
