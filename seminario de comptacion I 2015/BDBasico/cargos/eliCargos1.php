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
            <h1>Eliminar cargos</h1>
            <hr>
            <div class="col-sm-5">
            <form action="eliCargos2.php" method="post">
            <?php
		include ("../recursos/conecta.php");
		$bd = conectar();
		if (!$bd) return;
		$sql = "select codcar, nomcar from cargos order by nomcar";
		echo "<table class='table table-striped'>";
		echo "<tr><th>Seleccione un cargo</th> <th>Cargo</th> </tr>";
		$res = mysqli_query($bd,$sql);
		while($mat = mysqli_fetch_array($res)){
				echo "<tr>";
                                echo "<td> <input type='radio' name='victima' value='$mat[0]'> </td>";
				echo "<td> $mat[1] </td>" ;
				echo "</tr>" ;
		}
		mysqli_close($bd);
		echo "</table>";
            ?>
                <hr>
                <input type="submit" class="btn-danger btn-sm" value="Eliminar!">
            </form>
            </div>
        </div>
    </body>
</html>
