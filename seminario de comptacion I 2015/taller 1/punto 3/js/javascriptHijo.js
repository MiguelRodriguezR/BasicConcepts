window.addEventListener('message', function(event) {

        recibir(event.data)
 
});

var saludo = true;
var clave = false;
var retiro = false;
var digitos = [];

function recibir(boton){
	
	if(boton=="v"){
		if(saludo == true){
			saludo = false;
			clave = true;
			presentarClave();
		}
		else if(clave == true){
			ingresarClave();

		}
		else if(retiro == true){
			if(validarMonto()){
				retirarDinero();
			}
			

		}
	}


	if(boton=="a"){
		if(saludo == true){

		}
		else if(clave == true){

			if(digitos.length>=0){
				digitos.pop();
				ponerAsterisco();
			}

		}
		else if(retiro == true){

			if(digitos.length>=0){
				digitos.pop();
				ponerNumero();
			}
			
		}
	}



	if(boton=="r"){
		
			saludo = true;
			clave = false;
			retiro = false;
			digitos=[];
			presentarSaludo();
		
	}


	if(boton=="1"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=1;
				ponerAsterisco();
			}


		}
		else if(retiro == true){
			ingresarNumero(1);
		}
	}


	if(boton=="2"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=2;
				ponerAsterisco();
			}

		}
		else if(retiro == true){
			ingresarNumero(2);
		}
	}


	if(boton=="3"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=3;
				ponerAsterisco();
			}

		}
		else if(retiro == true){
			ingresarNumero(3);
		}
	}

	if(boton=="4"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=4;
				ponerAsterisco();
			}

		}
		else if(retiro == true){
			ingresarNumero(4);
		}
	}

	if(boton=="5"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=5;
				ponerAsterisco();
			}

		}
		else if(retiro == true){
			ingresarNumero(5);
		}
	}

	if(boton=="6"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=6;
				ponerAsterisco();
			}	

		}
		else if(retiro == true){
			ingresarNumero(6);
		}
	}

	if(boton=="7"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=7;
				ponerAsterisco();
			}

		}
		else if(retiro == true){
			ingresarNumero(7);
		}
	}

	if(boton=="8"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=8;
				ponerAsterisco();
			}

		}
		else if(retiro == true){
			ingresarNumero(8);
		}
	}

	if(boton=="9"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=9;
				ponerAsterisco();
			}

		}
		else if(retiro == true){
			ingresarNumero(9);
		}
	}

	if(boton=="0"){
		if(saludo == true){

		}
		else if(clave == true){
			if(digitos.length<4){
				digitos[digitos.length]=0;
				ponerAsterisco();
			}

		}
		else if(retiro == true){
			ingresarNumero(0);
		}
	}

}

  
function ingresarNumero(numero){

	if(digitos.length<6){
				digitos[digitos.length]=numero;
				ponerNumero();
			}
}

function ponerNumero(){
	str=""
	for (x in digitos){
		str+=digitos[x];
	}

	$("#ingreso").html(str); 

}


function presentarSaludo(){

	$("#pantalla").html("<h1>Bienvenido</h1><p>Oprima el boton verde para comenzar _</p>");
	$("#ingreso").html(""); 


}

function presentarClave(){

	$("#pantalla").html("<h2>Ingrese Clave :</h2><br>");
	$("#ingreso").html(""); 

}

function presentarRetiro(){

	$("#pantalla").html("<h2>Ingrese el monto a retirar :</h2><br>"); 
	$("#ingreso").html("");

}

function presentarPantallaClaveIncorrecta(){

	$("#pantalla").html("<h2>Clave Incorrecta :( </h2><br>");
		$("#ingreso").html("");

}

function presentarPantallaMontoIncorrectoMayor(){

	$("#pantalla").html("<h2>Debe ingresar un monto menor o igual a 500000 y mayor o igual a 10000</h2><br>");
		$("#ingreso").html("");

}

function presentarPantallaMontoIncorrectoNoModulo(){

	$("#pantalla").html("<h2>debe ingresar un monto multiplo de 5000 </h2><br>");
		$("#ingreso").html("");

}

function ponerAsterisco(){
	str=""
	for (x in digitos){
		str+="*";
	}

	$("#ingreso").html(str); 

}

function ingresarClave(){


	str=""
	for (x in digitos){
		str+=digitos[x];
	}
	if(str=="1234"){
		retiro = true;
		clave = false;
		presentarRetiro();
	}
	else{
		saludo = true;
		clave = false;
		presentarPantallaClaveIncorrecta();
		window.setTimeout(function(){
			presentarSaludo();},2000);
	}
	digitos=[];

}

function validarMonto(){

	str=""
	for (x in digitos){
		str+=digitos[x];
	}
	monto = parseInt(str);
	if(monto<=500000 && monto>=10000){
		if(monto%5000==0){
			return true;
		}
		else{
			presentarPantallaMontoIncorrectoNoModulo();
			window.setTimeout(function(){
			recibir("r");},2000);
			digitos=[];
			
			return false;
		}
	}
	else{
		presentarPantallaMontoIncorrectoMayor();
		window.setTimeout(function(){
		recibir("r");},2000);
		digitos=[];
		return false;
	}
	//$("#ingreso").html(str); 
}
function presentarPantallaTransaccionExitosa(){

	$("#pantalla").html("<h1>Transaccion Exitosa</h1><br>");
	$("#ingreso").html("");

}

function retirarDinero(){

	str=""
	for (x in digitos){
		str+=digitos[x];
	}
	monto = parseInt(str);
	billetes50=parseInt(monto/50000);
	monto-=50000*billetes50;
	billetes20=parseInt(monto/20000);
	monto-=20000*billetes20;
	billetes10=parseInt(monto/10000);
	monto-=10000*billetes10;
	billetes5=parseInt(monto/5000);
	monto-=5000*billetes5;

	array=[billetes50,billetes20,billetes10,billetes5]

	tiempodeEntrega=(billetes50+billetes20+billetes10+billetes5)*2000;

	window.parent.postMessage(array,'*');
	saludo = true;
		clave = false;
		presentarPantallaTransaccionExitosa();
		window.setTimeout(function(){
		recibir("r");},tiempodeEntrega);

}

presentarSaludo();