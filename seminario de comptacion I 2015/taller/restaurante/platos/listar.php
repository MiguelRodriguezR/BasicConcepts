<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Restaurante</title>
        <link href="../css/bootstrap.css" rel="stylesheet">
        <link href="../css/estilo.css" rel="stylesheet">
        <script src="../js/jquery.js"></script>
        <script src="../js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container">
            <?php
                include ("../recursos/navegacion.php");
            ?>
            <h1>Lista de Platos</h1>
            <hr>
            <?php
		include ("../recursos/coneccion.php");
		$bd = conectar();
		if (!$bd) return;
		$sql="SELECT * FROM platos,tipos WHERE tipos.id = platos.tipo";
		echo "<table class='table table-striped'>";
		echo "<tr><th>Nombre Plato</th> <th>Tipo</th>  <th>Valor</th> </tr>";
		$res = mysqli_query($bd,$sql);
		while($mat = mysqli_fetch_array($res)){
				echo "<tr>";
				echo "<td> $mat[1] </td>" ;
				echo "<td> $mat[5] </td>" ;
				echo "<td> $mat[3] </td>" ;
			                                
		}
		mysqli_close($bd);
		echo "</table>";
	?>
        </div>
    </body>
</html>
