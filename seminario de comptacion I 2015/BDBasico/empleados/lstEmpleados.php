<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Ejemplo basico BD</title>
        <link href="../css/bootstrap.css" rel="stylesheet">
        <link href="../css/estilo.css" rel="stylesheet">
        <script src="../js/jquery.js"></script>
        <script src="../js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container">
            <?php
                include ("../recursos/dibujaMenu.php");
            ?>
            <h1>Lista de empleados</h1>
            <hr>
            <?php
		include ("../recursos/conecta.php");
		$bd = conectar();
		if (!$bd) return;
		$sql = "select nomemp, numofi, nomcar, depend, telofi, exteofi from cargos, empleados where cargos.codcar = empleados.codcar order by depend";
		echo "<table class='table table-striped'>";
		echo "<tr><th>Nombre Empleado</th> <th>Oficina No</th>  <th>Cargo</th> <th>Dependencia</th>  <th>Telefono</th> </tr>";
		$res = mysqli_query($bd,$sql);
		while($mat = mysqli_fetch_array($res)){
				echo "<tr>";
				echo "<td> $mat[0] </td>" ;
				echo "<td> $mat[1] </td>" ;
				echo "<td> $mat[2] </td>" ;
				echo "<td> $mat[3] </td>" ;
				echo "<td> $mat[4] ($mat[5]) </td></tr>" ;                                
		}
		mysqli_close($bd);
		echo "</table>";
	?>
        </div>
    </body>
</html>
