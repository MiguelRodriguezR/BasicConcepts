$(document).ready(function() {
    // run the currently selected effect
    function runEffect() {
      // get effect type from
      var selectedEffect = "drop";
 
      // most effect types need no options passed by default
      var options = {};
      // some effects have required parameters
      if ( selectedEffect === "scale" ) {
        options = { percent: 100 };
      } else if ( selectedEffect === "size" ) {
        options = { to: { width: 280, height: 185 } };
      }
 
      // run the effect
      $( "#effect" ).show( selectedEffect, options,1000, callback );
    };
 
    //callback function to bring a hidden box back
    function callback() {
        $( "#effect:visible" )//.removeAttr( "style" ).fadeout();
    };
 
    $( "#effect" ).hide();
    runEffect();


    var respuestas = [6,4,3,5,5,2,6,1,3,3];
    var pregunta = 1;
    var preguntasr = [0,0,0,0,0,0,0,0,0,0];

   
         
    


    function saveR(respuesta){

      if(pregunta < 10){
          preguntasr[pregunta-1]= respuesta;
          //alert(preguntasr[pregunta])
          pregunta +=1;
          $("#p").attr("src","images/zad"+pregunta+".jpg");
          $("#r1").attr("src","images/"+pregunta+"_1.jpg");
          $("#r2").attr("src","images/"+pregunta+"_2.jpg");
          $("#r3").attr("src","images/"+pregunta+"_3.jpg");
          $("#r4").attr("src","images/"+pregunta+"_4.jpg");
          $("#r5").attr("src","images/"+pregunta+"_5.jpg");
          $("#r6").attr("src","images/"+pregunta+"_6.jpg");


      }

     
      else{
        preguntasr[pregunta]= respuesta;
        $( "#effect:visible" ).removeAttr( "style" ).fadeOut();
        window.setTimeout(function(){

         var promedio = 0;
         for(var x=0 ; x<10 ; x++){
          if(respuestas[x]==preguntasr[x]){
            promedio=promedio+1;  

          }
         }
         //alert(promedio);
         promedio = (promedio * 100)/10;
         document.getElementById("diag").innerHTML ="";
         document.getElementById("resp").innerHTML ="<h1>Usted ha contestado un "+promedio+"% de las preguntas correctamente</h1>";
         $( "#titulo" ).text( "RESULTADO" );
         runEffect();


    },500);
         

      }

    }

    $("#r1c").click(function(){
       saveR(1); 
    });
    $("#r2c").click(function(){
       saveR(2); 
    });
    $("#r3c").click(function(){
       saveR(3); 
    });
    $("#r4c").click(function(){
       saveR(4); 
    });
    $("#r5c").click(function(){
       saveR(5); 
    });
    $("#r6c").click(function(){
       saveR(6); 
    });

  });