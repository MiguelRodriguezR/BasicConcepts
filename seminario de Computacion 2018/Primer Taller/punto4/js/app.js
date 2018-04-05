var datos = {
  destino : "",
  fechaSalida : "",
  fechaLlegada : "",
  horaSalida : "",
  horaLlegada : "",
  lugarSalida : "",
  diasViaje : "",
  docenteResp:"",
  conductor:"",
  cantidadEstudiant:"",
  viaticosEstudiant:"",
  viaticosConductor:"",
  viaticosDocente:"",
  tipoACantidad:"",
  tipoACosto:"",
  tipoBCantidad:"",
  tipoBCosto:"",
  tipoCCantidad:"",
  tipoCCosto:"",
  placa:"",
  combustible:"",
  kilometrajeRecorrido:"",
  cantidadGalones:"",
  costoGalon:""

}




function getForm(num) {
  document.querySelector(".active").className = "hidden";
  document.querySelector("#f"+num).className = "active";
}

function setKilometros(){

  destino = document.querySelector("#destino").value;
  kilometros = document.querySelector("#kilometrajeRecorrido");
  destino= destino.split(":");
  kilometros.value = destino[1]+"km";
}

function actualizarDiasViaje() {
  llegada =  document.querySelector("#fechaLlegada").value
  salida = document.querySelector("#fechaSalida").value;
  resp = "Error ";

  if(llegada =="" || salida==""){
    resp = "complete campos de fechas";
  }
  else{
    resp = (new Date(llegada) - new Date(salida))/(1000*60*60*24) ;
  }
  if(resp<1){
    resp = "error dias de viaje negativos"
  }
  document.querySelector("#diasViaje").value = resp;

}

function getResum(){
  var resumenForm = document.querySelector("#f5");
  var resumen=""
  var errores="";
  var datosDados = true
  for(d in datos){
    var inputD = document.querySelector("#"+d)
    if(inputD.checkValidity()){
      datos[d]= inputD.value;
    }
    else{
      errores+="<br>* "+inputD.parentElement.textContent.split(':')[0];
      datos[d]="";
    }
    resumen+="<p>"+inputD.parentElement.textContent.split('\n')[0]+" <b>"+
    document.querySelector("#"+d).value+"</b></p>"
  }

  for(d in datos){
    if(datos[d]==""){
      datosDados = false
    }
  }



  if(datosDados){

    var costoViaticos = (
      (Number(datos.viaticosEstudiant)*Number(datos.cantidadEstudiant))
     +Number(datos.viaticosConductor)
     +Number(datos.viaticosDocente)
   )*Number(datos.diasViaje);

    var costoPeajes = (
      (Number(datos.tipoACantidad)*Number(datos.tipoACosto))
      +(Number(datos.tipoBCantidad)*Number(datos.tipoBCosto))
      +(Number(datos.tipoCCantidad)*Number(datos.tipoCCosto))
    );

    var costoCombustible = Number(datos.cantidadGalones)*Number(datos.costoGalon)

    var costoTotal= costoViaticos + costoPeajes + costoCombustible

    resumen+="<p class='total'> Valor Viaticos: $"+costoViaticos+" </p>";
    resumen+="<p class='total'> Valor Peajes: $"+costoPeajes+" </p>";
    resumen+="<p class='total'> Valor Combustible: $"+costoCombustible+" </p>";
    resumen+="<p class='total'> Valor total de la practica: $"+costoTotal+" </p>";
    if(isNaN(costoTotal))resumen="<div class='error'><p> Fechas mal programadas </p></div>"

  }

  else{
    resumen="<div class='error'><p> Por favor rellene todos los datos e ingrese de manera valida los siguientes valores:</p>";
    resumen+=errores+"</div>";
  }


  resumenForm.innerHTML=resumen;
  getForm(5);
}

function resetear() {
  document.querySelector('form').reset();
  getForm(1);
}
