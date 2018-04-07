$(document).ready(function(){
  $("form").submit(function(evt){
    evt.preventDefault();
    var value = $("input").val();
    var resp= value+" en romanos es: "+romanize(value)
    $("#resp").html(resp);
  });
});

function romanize (num) {
  var dictionary =
    { M:1000,
      CM:900,
      D:500,
      CD:400,
      C:100,
      XC:90,
      L:50,
      XL:40,
      X:10,
      IX:9,
      V:5,
      IV:4,
      I:1
    };
  var roman = '';
  var i;
  for ( i in dictionary ) {
    while ( num >= dictionary[i] ) {
      console.log("numero:"+num+" romano:"+i+" se quitará: "+dictionary[i]);
      roman += i;
      num -= dictionary[i];
    }
  }
  return roman;
}
