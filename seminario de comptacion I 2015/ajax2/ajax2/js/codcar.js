$(document).ready(function(){
    
    $("#frmcar").submit(function(evt){
        evt.preventDefault();
        
        $.ajax({
            url: "cargos.php",
            type: "post",
            data: $("#frmcar").serialize(),
            beforeSend: function(){
                $("#divcar").html("<img src='ajax-loader.gif'>");
            },
            success: function (datos) {
                $("#divcar").html(datos);
            }
        });
        
    });
    
});

