$(document).ready(
        function(){
         
            var x="Julian Portilla";
            var c;
            var b=0;
            var a=0;
            //$("#txt1").val(10);
            
            //document.getElementById("btn1");
           // $("#btn1").click(//como se programa un boton combencional 
           $("#frm1").submit( // valida los campos en el formulario
                    function(evt){
                        evt.preventDefault();
                        a=parseInt($("#txt1").val());
                        b=parseFloat($("#txt2").val());
                        x=$("#lstope").val();
                        if(x=="+"){c=a+b;}   
                        else if(x=="-"){c=a-b;}
                        else if(x=="*"){c=a*b;}
                        else if(x=="/" && b!=0){c=a/b;}
                        
                        alert("Resultado: "+c);
                        
                        
                    });
        });