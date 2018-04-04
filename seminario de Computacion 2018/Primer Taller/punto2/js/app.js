var preguntas = {
  1:[
    "Tres paquetes tienen 5 galletas cada uno. La cantidad de galletas que"+
     " hay en total se puede expresar como",
     "5",
     "5 + 5 + 5",
     "3 + 5",
     "3 + 3 + 3",
     "B"
   ],
   2:[
     "De lunes a jueves, Valeria deposita diariamente 3 monedas en su alcancía."+
     " ¿Cuántas monedas ha depositado Valeria durante estos 4 días?",
     "3",
     "4",
     "7",
     "12",
     "D"
   ],
   3:[
     "Diana tenía 5 dulces y Pedro tenía 3. Luego Roberto le regaló 2" +
     " dulces a cada uno.¿Cuál de las siguientes afirmaciones es correcta?",
     "Quien tenía más dulces sigue teniendo más",
     "Ahora los dos tienen menos dulces que antes.",
     "Ahora los dos tienen la misma cantidad de dulces.",
     "Quien tenía más dulces, ahora tiene menos.",
     "A"
   ],
   4:[
     "Diez niños de un grupo votaron por el color que querían para el" +
     " uniforme de su equipo de atletismo. "+
     " El color más votado será el de la camiseta y el segundo más votado,"+
     " el de la pantaloneta.<br>"+
     "Estos fueron los resultados:<br>"+
     "<b>Azul, rojo, negro, azul, verde, azul, gris, blanco, blanco, amarillo.</b><br>"+
     "Los colores de la camiseta y la pantaloneta deben ser",
     "azul y blanco.",
     "azul y rojo.",
     "blanco y negro.",
     "negro y azul.",
     "A"
   ],
   5:[
     "En una escuela deportiva, el año pasado había 45 inscritos."+
      "Este año hay 69. Eso significa que del año pasado a este",
      "se retiraron 14 personas.",
      "se inscribieron 14 personas más.",
      "se retiraron 24 personas.",
      "se inscribieron 24 personas más.",
      "D"
   ],
   6:[
     "A la fiesta de Carlos asistieron en principio 25 personas, "+
     "luego llegaron 13 personas más. ¿Cuántas personas en total asistieron a la fiesta?",
     "12",
     "13",
     "25",
     "38",
     "D"
   ],
   7:[
     "Estas son las frutas preferidas de 11 niños.<br>"+
     "<b>Fresa, banano, manzana, piña, manzana, manzana, manzana,"+
     "fresa, manzana, manzana, uva.</b><br>"+
     "¿Cuál es la fruta preferida por la mayoría de niños de este grupo?",
     "Fresa.",
     "Manzana",
     "Piña.",
     "Uva.",
     "B"
   ],
   8:[
     "Al comenzar el año, Daniel tenía 8 lápices y ha perdido 5. "+
     "¿Cuántos lápices tiene ahora?",
     "3",
     "5",
     "8",
     "13",
     "A"
   ],
   9:[
     "Tomás debe escoger una de cuatro rutas posibles para ir de su casa al parque."+
     "La ruta 2 es más corta que la 1."+
     "La ruta 2 es más corta que la 3."+
     "La ruta 4 es igual de larga que la 1.<br>"+
     "¿Cuál es la ruta más corta que puede escoger Tomás?",
     "La 1.",
     "La 2.",
     "La 3.",
     "La 4.",
     "B"
   ],
   10:[
     "Francisco pagó un helado con una moneda de $500 y otra de $200 y no le sobró dinero."+
     "Si Francisco hubiera pagado con un billete de $1.000, le habría sobrado",
     "$100",
     "$200",
     "$300",
     "$500",
     "C"
   ]
}

window.onload = function(){
  var form = document.querySelector("form");
  for (var x in preguntas){
    form.innerHTML+=
    "<div class='pregunta' id='p"+x+"'>"+
      "<p>"+
        preguntas[x][0]+
      "</p>"+
      "<input type='radio' name='"+x+"' value='A'>"+
      "A) "+preguntas[x][1]+"<br>"+
      "<input type='radio' name='"+x+"' value='B'>"+
      "B) "+preguntas[x][2]+"<br>"+
      "<input type='radio' name='"+x+"' value='C'>"+
      "C) "+preguntas[x][3]+"<br>"+
      "<input type='radio' name='"+x+"' value='D'>"+
      "D) "+preguntas[x][4]+"<br>"+
    "</div>";
  }
}

function calificar() {
  var correctas=0,incorrectas=0;
  for (var x in preguntas){
    var radio = document.querySelectorAll('input[name="'+x+'"]');
    var correcto = false;
    radio.forEach(function(r){
	      if(r.checked){
          if(r.value == preguntas[x][5]){
            correcto = true;
          }
        }
    });
    if(correcto) {
      radio[0].parentElement.className="pregunta correcto";
      correctas++;
    }

    else {
      radio[0].parentElement.className="pregunta incorrecto";
      incorrectas++;
    }

  }
  document.querySelector('#total').innerHTML ="<p id='buenas'></p><p id='malas'></p>"+
    "<p>Calificacion: "+((correctas*5.0)/(correctas+incorrectas))+"</p>";
  document.querySelector('#buenas').innerHTML = "Respuestas Correctas: "+correctas;
  document.querySelector('#malas').innerHTML = "Respuestas Incorrectas: "+incorrectas;
  document.querySelector('button').hidden = true;
}
