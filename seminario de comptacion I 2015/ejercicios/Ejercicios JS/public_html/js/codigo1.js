$(document).ready(
        function(){
         
          
            //$("#txt1").val(10);
            
            //document.getElementById("btn1");
           // $("#btn1").click(//como se programa un boton combencional 
           $("#form1").submit( // valida los campos en el formulario
                    function(evt){
                        
                        evt.preventDefault();
                        var tiempo =0;
                        var distancia =0;
                        var respuesta;
                        tiempo = parseInt($("#tiempo").val());
                        distancia = parseInt($("#distancia").val());
                        respuesta="la velocidad es:"+distancia/tiempo+"Km/hora";
                        document.getElementById("respuesta").innerHTML=respuesta;
                        
                        
                        
                        
                    });
                    
            $("#form2").submit( // valida los campos en el formulario
                    function(evt){
                        
                        evt.preventDefault();
                        var precio =0;
                        var cantidad =0;
                        var respuesta;
                        var porcentaje=0;
                        var tarifa=0;
                        var total=0;
                        precio = parseInt($("#precio").val());
                        cantidad = parseInt($("#cantidad").val());
                        if(cantidad <= 5){
                            respuesta="el valor total es: "+cantidad*precio;
                        }
                        else if(cantidad > 5 && cantidad < 10){
                            tarifa=(cantidad*precio);
                            porcentaje =(cantidad*precio*0.05);
                            total= (cantidad*precio)-(cantidad*precio*0.05);
                            respuesta="el valor total es: "+total;
                        }
                         else if( cantidad > 10){
                            respuesta="el valor total es: "+(cantidad*precio)-(cantidad*precio*0.2);
                        }
      
                        document.getElementById("respuesta").innerHTML=respuesta;
                        
                        
                        
                        
                    });
        });