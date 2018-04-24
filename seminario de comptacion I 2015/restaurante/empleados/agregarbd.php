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
                include ("../recursos/navegacion.php");
                $ced = $_POST['txtced'];
        		$nom = $_POST['txtnom'];
        		$car = $_POST['lstcar'];
		
		
		include("../recursos/coneccion.php");
		$bd = conectar();
		if (!$bd) return;
		$sql = "INSERT into empleados values ( '$nom' , '$ced', '$car' )";
		$res = mysqli_query($bd,$sql);
                if ($res) {
                   echo "<div class='alert alert-success' role='alert'><strong>Atención</strong> Registro adicionado con éxito</div>";
                }
                else {
                    echo "<div class='alert alert-danger' role='alert'><strong>Error</strong> Registro NO adicionado";
                    echo " - " .  mysqli_error($bd)  . "</div>";
                }
		mysqli_close($bd);
            ?>
        </div>
    </body>
</html>