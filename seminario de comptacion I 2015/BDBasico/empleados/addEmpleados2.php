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
                $ced = $_POST['txtced'];
		$nom = $_POST['txtnom'];
		$ofi = $_POST['lstofi'];
		$car = $_POST['lstcar'];
		$tel = $_POST['txttel'];
		$ext = $_POST['txtext'];
		
		
		include("../recursos/conecta.php");
		$bd = conectar();
		if (!$bd) return;
		$sql = "insert into empleados values ('$ced' ,'$nom', '$ofi', '$car', '$tel', '$ext')";
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