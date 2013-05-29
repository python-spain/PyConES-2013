;(function () {
  var showMessage = function(msgId, message, cls) {
      $(msgId).html('<p class="' + cls + '">' + message + '</p>')
              .show()
              .delay(3000)
              .fadeOut();
  };

  $('#subscribe-newsletter').click(function(e){
      e.preventDefault();

      var form = $("#newsletter-form");

      $.post(form.attr('action'), form.serialize(), null, 'json')
       .done(function(data){
           showMessage("#newsletter-message", data.message, "alert alert-success");
        })
       .fail(function(data) {
           var responseJSON = JSON.parse(data.responseText);
           showMessage("#newsletter-message", responseJSON.message, "alert alert-error");
       });
  });

  $('#contact-us').click(function(e){
      e.preventDefault();

      var form = $("#contact-us-form");

      $.post(form.attr('action'), form.serialize(), null, 'json')
       .done(function(data){
           showMessage("#contact-us-message", data.message, "alert alert-success");
       })
       .fail(function(data){
           var responseJSON = JSON.parse(data.responseText);
           showMessage("#contact-us-message", responseJSON.message, "alert alert-error");
       });
   });

  // Sliders
  $('#patrocinadores-slides').flexslider({
      controlsContainer: '.patrocinadores-nav',
      manualControls: '.patrocinadores-nav li'
   });

  $('#informacion-slides').flexslider({
      controlsContainer: '.nav-datos',
      manualControls: '.nav-datos li'
   });
  // Fin sliders

  // Code_of_conduct javascript
  $('#conduct-link').on('click',toggleCodeOfConduct);
  $('#close-conduct1-link , #close-conduct2-link').on('click',toggleCodeOfConduct);

  function toggleCodeOfConduct(){
    coc = $('#code_of_conduct');
    if(coc.css('display') == 'none'){
        coc.slideDown(1500);
    }else{
        coc.slideUp(700);
    }
   }
  // Fin Code_of_conduct javascript

})();



