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
           $('#newsletter-form input[type=text]').val('');
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
           $('#contact-us-form input[type=text], #contact-us-form textarea').val('');
       })
       .fail(function(data){
           var responseJSON = JSON.parse(data.responseText);
           showMessage("#contact-us-message", responseJSON.message, "alert alert-error");
       });
   });

  $('.more-info-footer').click(function(e){
      e.preventDefault();
      var href = $(this);
      var divToToggle = $('#text-' + href[0].id);
      toggleMoreInfoFooter(divToToggle);
  });

  $('#close-legal-terms').click(function(e){
      e.preventDefault();
      var divToToggle = $('#text-legal-terms');
      toggleMoreInfoFooter(divToToggle);
  });

  $('#close-code-of-conduct').click(function(e){
      e.preventDefault();
      var divToToggle = $('#text-code-of-conduct');
      toggleMoreInfoFooter(divToToggle);
  });

  function toggleMoreInfoFooter(divToToggle){
      if(divToToggle.css('display') == 'none'){
          divToToggle.slideDown(1500);
      } else {
          divToToggle.slideUp(1500);
      }
  }

  // Sliders
  $('#patrocinadores-slides').flexslider({
      manualControls: '.patrocinadores-nav li'
   });

  $('#informacion-slides').flexslider({
      manualControls: '.nav-datos li'
   });
  // Fin sliders

  // setLang
  $('#setLang a').click(function(e){
    e.preventDefault();
    var lang = $(this).attr('data-lang');
    $('#language').val(lang);

    var form = $("#setLang");
    form.submit();
  });

  // schedule toggle
  $('#agenda ul.schedule-list li').on('click',function(event){
    $(this).find('div').toggle();
  });

})();



