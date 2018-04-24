$(document).ready(
	 function(){
	 	 var placas=[];
         var horasEntrada=[];
         var horasSalida=[];
         var minutosEntrada=[];
         var minutosSalida=[];
         var tarifas=[];
         var costosTotales=[];
         var tipos=[];
         var seleccionado;

         $("#registrar").submit(
         	function(evt){
         		evt.preventDefault();
         		//alert($("#pl").val());

         		if($("#sel_camion").hasClass("card active")){
         			seleccionado="camion";
         		}
         		else if($("#sel_carro").hasClass("card active")){
         			seleccionado="carro";
         		}
         		else if($("#sel_moto").hasClass("card active")){
         			seleccionado="moto";
         		}

         		placas[placas.length]=$("#pl").val();
         		horasSalida[horasSalida.length]=$("#hs").val();
         		horasEntrada[horasEntrada.length]=$("#he").val();
         		minutosSalida[minutosSalida.length]=$("#ms").val();
         		minutosEntrada[minutosEntrada.length]=$("#me").val();
         		if($("#ta").val()==""){
         			if(seleccionado=="camion"){tarifas[tarifas.length]=2400.0;}
         			else if(seleccionado=="carro"){tarifas[tarifas.length]=1800.0;}
         			else if(seleccionado=="moto"){tarifas[tarifas.length]=600.0;}	
         		}
         		else{
         			tarifas[tarifas.length]=parseFloat($("#ta").val());
         		}
         		tipos[tipos.length]=seleccionado;
         		var tiempoTranscurrido=((parseFloat($("#hs").val())*60)+parseFloat($("#ms").val()))-((parseFloat($("#he").val())*60)+parseFloat($("#me").val()));

         		costosTotales[costosTotales.length]=(parseFloat(tarifas[tarifas.length-1])*tiempoTranscurrido)/60;
         		var str="<br><div class='info'><h1>MOTOS</h1></div><br>";
         		str+="<table class='tabla'><tr><td>Placa</td><td>HE</td><td>HS</td><td>Costo</td></tr>";
         		var total=0;
         		var granTotal=0;
         		for(var i=0 ; i<placas.length ; i++ ){
         			if(tipos[i]=="moto"){
         				str+="<tr><td>"+placas[i]+" </td><td> "+horasEntrada[i]+":"+minutosEntrada[i]+" </td><td> "+horasSalida[i]+":"+minutosSalida[i]+ "</td><td> "+costosTotales[i]+" </td></tr> ";
         				total+=costosTotales[i];
         			}
         			
         		}
         		str+="<tr><td>TOTAL:"+total+"</td></tr></table>";
         		str+="<br><div class='info'><h1>AUTOMOVILES</h1></div><br>";
         		str+="<table class='tabla'><tr><td>Placa</td><td>HE</td><td>HS</td><td>Costo</td></tr>";
         		granTotal+=total;
         		total=0;
         		for(var i=0 ; i<placas.length ; i++ ){
         			if(tipos[i]=="carro"){
         				str+="<tr><td>"+placas[i]+" </td><td> "+horasEntrada[i]+":"+minutosEntrada[i]+" </td><td> "+horasSalida[i]+":"+minutosSalida[i]+ "</td><td> "+costosTotales[i]+" </td></tr> ";
         				total+=costosTotales[i];
         			}
         			
         		}
         		str+="<tr><td>TOTAL:"+total+"</td></tr></table>";
         		str+="<br><div class='info'><h1>CAMIONES</h1></div><br>";
         		str+="<table class='tabla'><tr><td>Placa</td><td>HE</td><td>HS</td><td>Costo</td></tr>";
         		granTotal+=total;
         		total=0;
         		for(var i=0 ; i<placas.length ; i++ ){
         			if(tipos[i]=="camion"){
         				str+="<tr><td>"+placas[i]+" </td><td> "+horasEntrada[i]+":"+minutosEntrada[i]+" </td><td> "+horasSalida[i]+":"+minutosSalida[i]+ "</td><td> "+costosTotales[i]+" </td></tr> ";
         				total+=costosTotales[i];
         			}
         			
         		}
         		str+="<tr><td>TOTAL:"+total+"</td></tr></table>";
         		granTotal+=total;
         		str+="<br><div class='info'><h1>GRAN TOTAL:"+granTotal+"</h1></div><br>";

         		$("#tabla").html(str);

         	});
	 });