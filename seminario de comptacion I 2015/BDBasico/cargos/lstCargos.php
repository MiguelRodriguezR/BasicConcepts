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
            <h1>Lista de cargos</h1>
            <hr>
            <?php
		include ("../recursos/conecta.php");
		$bd = conectar();
		if (!$bd) return;
		$sql = "select * from cargos order by nomcar";
		echo "<table class='table table-striped'>";
		echo "<tr><th>Código de cargo</th> <th>Cargo</th>  <th>Dependencia</th>  </tr>";
		$res = mysqli_query($bd,$sql);
		while($mat = mysqli_fetch_array($res)){
				echo "<tr>";
				echo "<td> $mat[0] </td>" ;
				echo "<td> $mat[1] </td>" ;
				echo "<td> $mat[2] </td></tr>" ;
		}
		mysqli_close($bd);
		echo "</table>";
	?>
        </div>
    </body>
</html>
