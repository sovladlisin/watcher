$(document).ready(function(){
      $('#exit').on('click', function(event){
          event.preventDefault();
          $('.wall').addClass('is-visible');
      });

      //close popup
        $('.wall').on('click', function(event){
            if( $(event.target).is('#exit') || $(event.target).is('.wall')) {
                event.preventDefault();
                $(this).removeClass('is-visible');
            }
        });

});
