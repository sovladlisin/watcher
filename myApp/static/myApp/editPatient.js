$(document).ready(function(){
    $(".form-add").find("input").hover(function(){
               $(this).css("transition","0.2s");
               $(this).next(".hidden-line").css("background-color","rgb(29, 119, 100)");
               $(this).css("background-color","rgb(198, 198, 198)");
          },
              function(){
              $(this).css("transition","1.5s");
              $(this).next(".hidden-line").css("background-color","rgb(39,166,142)");
               $(this).css("background-color","rgb(255, 255, 255)");
          });
    $(".form-add").find("select").hover(function(){
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