$(document).ready(function(){
    $(".line").click(function(){
        if($(this).next().is(':visible')) {
            $(".info").slideUp();
            $(".hidden-line").slideUp();
            $(".line").css("opacity","1");
            $(".line").css("background-color","rgb(255, 255, 255)");
            $(".line").css("color","black");

        }
        else{
            $(".info").slideUp();
            $(".line").css("opacity","0.2");
            $(".line").css("background-color","rgb(255, 255, 255)");
            $(".hidden-line").slideUp();

            $(this).css("opacity","0");
            $(this).next(".hidden-line").slideDown();
            $(this).next().next().slideDown();



        }
    });
      $(".line").hover(function(){
           $(this).css("transition","0.2s");
           $(this).next(".hidden-line").css("background-color","rgb(29, 119, 100)");
           $(this).css("background-color","rgb(198, 198, 198)");
      },
          function(){
          $(this).css("transition","1.5s");
          $(this).next(".hidden-line").css("background-color","rgb(39,166,142)");
           $(this).css("background-color","rgb(255, 255, 255)");
      });
});
