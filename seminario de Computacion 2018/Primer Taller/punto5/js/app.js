const productos = {
  "1":["Zapato Casual Mujer Pikolinos Z0K8 Café","$ 699.900"],
  "2":["Zapato Casual Mujer Pikolinos Z0K7 Café","$ 699.900"],
  "3":["Bota Casual Mujer Pikolinos BBZ2 Vino Tinto","$ 969.900"],
  "4":["Sandalia Casual Mujer Franco Sarto SDSU Caramelo","$ 499.900"],
  "5":["Zapato Casual Hombre Freeport ZMDL Castaño Claro","$ 399.900"],
  "6":["Zapato Casual Hombre Sperry ZMC7 Azul Oscuro","$ 499.900"],
  "7":["Tenis Casuales Hombre Camper ZL3D Blanco	","$ 699.900"],
  "8":["Zapato Casual Hombre Sperry ZMC5 Caramelo","$ 599.900"]
}
var carro = [];



function mostrarProductos(){
  var $contenedor = $('#contenedorProductos');
  resultado = ""
  for(var x in productos){
    resultado+="<div class='producto'>"+
    "<img src='images/"+x+".jpg' >"+
      "<div class='descripcion'>"
        +productos[x][0]+"<br>"+productos[x][1]+
      "</div>"+
      "<button id='btn-"+x+"' class='agregarBtn'>Agregar al carrito</button>"+
    "</div>"
  }
  $contenedor.html(resultado);
}

function agregarAlCarro(producto){
  var addone = true;
  carro.forEach((p)=>{
    if(p[2]==producto){
      console.log(p[3]);
      p[3]=p[3]+1;
      addone = false;
    }
  })
  if(addone){
    for(var x in productos){
      if(Number(x) == Number(producto)){
        carro.push([...productos[x],x,1]);
        console.log(carro);
      }
    }
  }
  $carrito = $("#carritoProductos");
  respuesta = '';
  carro.forEach((p)=>{
    respuesta+=
    "<a class='productoCarrito'><span>"+
    p[0]+"</span><span> Cantidad "+p[3]+
    "</span></a>";

  });
  $carrito.html(respuesta);
}


$(document).ready(function(){
  mostrarProductos();
  $('#openBtn').click(()=>{
    $('#carrito').css('width','20%');
  });
  $('#closeBtn').click(()=>{
    $('#carrito').css('width','0px');
  });
  $(document).on("click",".agregarBtn", function () {
   var clickedBtnID = $(this).attr('id');
   clickedBtnID = clickedBtnID.split("-")
   clickedBtnID = clickedBtnID[1];
   agregarAlCarro(clickedBtnID);
  });
});
