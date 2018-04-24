<?php

	$p1=$_POST["p1"];
	$p2=$_POST["p2"];
	$p3=$_POST["p3"];
	$p4=$_POST["p4"];
	$p5=$_POST["p5"];
	$p6=$_POST["p6"];
	$p7=$_POST["p7"];
	$p8=$_POST["p8"];
	$p9=$_POST["p9"];
	$p10=$_POST["p10"];
	$aspirante=$_POST["aspirante"];
	$test=$_POST["test"];
	$calificacion=($p1+$p2+$p3+$p4+$p5+$p6+$p7+$p8+$p9+$p10)/10;
	include ("recursos/conecta.php");
    $bd = conectar();
    if (!$bd) return;

    $sql="SELECT * FROM aspirantes INNER JOIN cargo on aspirantes.cargo = cargo.id JOIN perfil on cargo.id = perfil.id WHERE aspirantes.cedula='$aspirante'";
    $res = mysqli_query($bd,$sql);
	$arr=mysqli_fetch_array($res);
	$perfil=$arr[10];
	$minima=$arr[9];



    $sql = "SELECT test FROM entrevistas WHERE entrevistas.test='$test' and entrevistas.aspirante='$aspirante' ";
	$res = mysqli_query($bd,$sql);
	$arr=mysqli_fetch_array($res);
	if($arr[0] != "" ){
		echo "<div class='alert alert-danger' role='alert'><strong>Error</strong> Registro ya ha sido adicionado";
		return;
	}

    $sql = "INSERT into entrevistas (aspirante,calificacion,test) values ( '$aspirante' , '$calificacion' , '$test')";
	$res = mysqli_query($bd,$sql);
	if ($res==1) {
        echo "<div class='alert alert-success' role='alert'><strong>Atención</strong> Registro adicionado con éxito</div>";
        }
    else {
        echo "<div class='alert alert-danger' role='alert'><strong>Error</strong> Registro NO adicionado";
        echo " - " .  mysqli_error($bd)  . "</div>";
        }
    $sql2 = "SELECT * FROM entrevistas WHERE entrevistas.aspirante='$aspirante'";
    $res2 = mysqli_query($bd,$sql2);
    $contador=0;
    $calificacion=0;
    while($arr2=mysqli_fetch_array($res2)){
    	$calificacion=$calificacion+$arr2[2];
    	$contador+=1;
    }

    $estado=0;

   

    $calificacion=$calificacion/$contador;
     if($calificacion>5*$minima){
    	$estado=1;
    }
    else{
    	$estado=2;
    }
    $sql3 = "UPDATE aspirantes set aspirantes.calificacion='$calificacion' WHERE aspirantes.cedula='$aspirante' ";
    $res3 = mysqli_query($bd,$sql3);
     $sql3 = "UPDATE aspirantes set aspirantes.estado='$estado' WHERE aspirantes.cedula='$aspirante' ";
    $res3 = mysqli_query($bd,$sql3);

    if($res3!=1) {
    	echo "<div class='alert alert-danger' role='alert'><strong>Error</strong> Registro NO adicionado";
    	echo " - " .  mysqli_error($bd)  . "</div>";
    }



	/*echo $p1;
	echo $p2;
	echo $p4;
	echo $p6;
	echo $aspirante;*/



?>