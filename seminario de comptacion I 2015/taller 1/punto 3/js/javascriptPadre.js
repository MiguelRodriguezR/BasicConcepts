
$(document).ready(

	 function(){
	 var frame = document.getElementById('iframe');

	 	$("#bv").click(function(){ frame.contentWindow.postMessage("v",'*');});
	 	$("#ba").click(function(){ frame.contentWindow.postMessage("a",'*');});
	 	$("#br").click(function(){ frame.contentWindow.postMessage("r",'*');});

	 	$("#b1").click(function(){ frame.contentWindow.postMessage("1",'*');});
	 	$("#b2").click(function(){ frame.contentWindow.postMessage("2",'*');});
	 	$("#b3").click(function(){ frame.contentWindow.postMessage("3",'*');});

	 	$("#b4").click(function(){ frame.contentWindow.postMessage("4",'*');});
	 	$("#b5").click(function(){ frame.contentWindow.postMessage("5",'*');});
	 	$("#b6").click(function(){ frame.contentWindow.postMessage("6",'*');});

	 	$("#b7").click(function(){ frame.contentWindow.postMessage("7",'*');});
	 	$("#b8").click(function(){ frame.contentWindow.postMessage("8",'*');});
	 	$("#b9").click(function(){ frame.contentWindow.postMessage("9",'*');});

	 	$("#b0").click(function(){ frame.contentWindow.postMessage("0",'*');});
	 
	 	
});



$(function() {

	window.addEventListener('message', function(event) {

        recibirArray(event.data);
 
	});

	var tiempo=0;

	function recibirArray(array){

			//alert(array);
			for(x in array){
				entregarbillete(x,array[x]);
			}
			tiempo=0;
	}

	function entregarbillete(valorbillete , cantidad){

		var image;
		if(valorbillete==0){image="images/50000.jpeg"}		
		if(valorbillete==1){image="images/20000.jpeg"}
		if(valorbillete==2){image="images/10000.jpeg"}		
		if(valorbillete==3){image="images/5000.jpeg"}
		

		for(x=0 ; x<cantidad ; x++){
			 window.setTimeout(function(){
			 	$("#ima").attr("src",image);
			 	
			 	runEffect();
			 },tiempo);
			 tiempo+=2000;
		}

	}

    // run the currently selected effect
    function runEffect() {
      // get effect type from
      var selectedEffect = "clip";
 
      // most effect types need no options passed by default
      var options = {};
      // some effects have required parameters
      if ( selectedEffect === "scale" ) {
        options = { percent: 100 };
      } else if ( selectedEffect === "size" ) {
        options = { to: { width: 280, height: 185 } };
      }
 
      // run the effect
      $( "#effect" ).show( selectedEffect, options, 500, callback );
    };
 
    //callback function to bring a hidden box back
    function callback() {
      setTimeout(function() {
        $( "#effect:visible" ).removeAttr( "style" ).fadeOut();
      }, 1000 );
    };
 
    // set effect from select menu value
    $( "#button" ).click(function() {
      
    });

   
 
    $( "#effect" ).hide();
    //runEffect();
  });

