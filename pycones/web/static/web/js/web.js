;(function () {
  $('#subscribe-newsletter').click(function(e){
      e.preventDefault();

      var showMessage = function(message, cls) {
        $('#newsletter-message').html('<p class="' + cls + '">' + message + '</p>')
                                .show()
                                .delay(3000)
                                .fadeOut();

      };

      var form = $("#newsletter-form");

      $.post(form.attr('action'), form.serialize(), null, 'json')
       .done(function(data){
         showMessage(data.message, "alert alert-success");
        })
       .fail(function(data) {
          showMessage(data.responseJSON.message, "alert alert-error");
        });
  });
})();
