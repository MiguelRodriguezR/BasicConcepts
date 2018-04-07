var slideIndex = 2;

var descriptions = [
  "<b>Monster 1200s</b><br> Marca : Ducati<br>Cilindraje : 1200cc<br>Uso: Traveling",
  "<b>R1</b><br> Marca : Yamaha<br>Cilindraje : 998cc<br>Uso: Competencia",
  "<b>XJ6</b><br> Marca : Yamaha<br>Cilindraje : 600cc<br>Uso: City Bike - Naked",
  "<b>R6</b><br> Marca : Yamaha<br>Cilindraje : 599cc<br>Uso: City Bike",
  "<b>Ninja</b><br> Marca : Kawasaki<br>Cilindraje : 300cc<br>Uso: City Bike",
  "<b>Monster 796s</b><br> Marca : Ducati<br>Cilindraje : 796cc<br>Uso: Traveling",
]



$(document).ready(function(){
  showSlides(slideIndex);
  $('#leftButton').click(()=>{pasar(-1)});
  $('#rightButton').click(()=>{pasar(1)});
});

function showSlides(slide) {
  var slider = $("#slider");

  var posLeft = slide-1;
  var posRight = slide+1;
  if(slide==0){
    posLeft = descriptions.length-1;
  }
  if(slide==descriptions.length-1){
    posRight = 0;
  }
  var left = "<img class='left' src='images/p"+posLeft+".jpg' >";
  var actual = "<img class='actual' src='images/p"+slide+".jpg' >";
  var right = "<img class='right' src='images/p"+posRight+".jpg' >";
  slider.html(left+actual+right);

  var descContainer = $(".desc-Container");
  descContainer.html("<h3>"+descriptions[slide]+"</h3>");
}

function pasar(towhere){
  if(towhere=="-1" && slideIndex==0) slideIndex=descriptions.length-1;
  else if(towhere=="1" && slideIndex==descriptions.length-1) slideIndex=0;
  else if(towhere=="1") slideIndex++;
  else slideIndex--;
  showSlides(slideIndex);
}
