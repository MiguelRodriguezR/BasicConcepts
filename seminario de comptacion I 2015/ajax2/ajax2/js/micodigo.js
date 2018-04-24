function llamar(x){
    //alert (x);
      $("#divres1").html("<img src='ajax-loader.gif'>");
      $("#divres1").load("tarea2.php?var="+x);
}

$(document).ready(function(){
    
    $("#op1").click(function(evt){
        evt.preventDefault();
        //llamado ajax
        $("#divres").html("<img src='ajax-loader.gif'>");
        $("#divres").load("desarrollador.html");
    });
    $("#op2").click(function(evt){
        evt.preventDefault();
        //llamado ajax
        $("#divres").html("<img src='ajax-loader.gif'>");
        $("#divres").load("empleados.php");
    });
    
    $("#op3").click(function(evt){
        evt.preventDefault();
        //llamado ajax
        $("#divres").html("<img src='ajax-loader.gif'>");
        $("#divres").load("cargos.html");
    });
    
    $("#op4").click(function(evt){
        evt.preventDefault();
        //llamado ajax
        $("#divres").html("<img src='ajax-loader.gif'>");
        $("#divres").load("tarea.php");
    });
});
