function subscribeNewsletter(){
    $('#subscribe-newsletter').live('click', function(e){
        e.preventDefault();
        var form = $("#newsletter-form");
        $.post(form.attr('action'), form.serialize(), function(data){
            $('#newsletter-message')[0].innerText = data.message;
            //Falta hacer desaparecer el mensaje tras unos segundos 
        }, 'json');
    });
}

function main() {
    subscribeNewsletter();
}
$(document).ready(main);

