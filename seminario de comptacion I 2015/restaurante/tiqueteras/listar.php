<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Restaurante</title>
        <link href="../css/bootstrap.css" rel="stylesheet">
        <link href="../css/estilo.css" rel="stylesheet">
        <link href="../css/dataTables.min.css" rel="stylesheet">   
        <script src="../js/jquery.js"></script>
        <script src="../js/bootstrap.min.js"></script>
        <script src="../js/dataTables.min.js"></script>
        
    </head>
    <body>
        <div class="container">
            <?php
                include ("../recursos/navegacion.php");
            ?>
            <h1>Lista de tiqueteras</h1>
            <hr>
            <?php
    		include ("../recursos/coneccion.php");
    		$bd = conectar();
    		if (!$bd) return;
    		$sql="SELECT * FROM tiqueteras,tipos WHERE tipos.id = tiqueteras.tipo";

    		echo "<table id='example' class='table table-striped display'><thead>";
    		echo "<tr><th>Cliente</th> <th>Cedula</th> <th>Tamaño</th> <th>Consumo</th> <th>Tipo</th> <th>Detalle</th> </tr></thead><tbody>";
    		$res = mysqli_query($bd,$sql);
    		while($mat = mysqli_fetch_array($res)){
    				echo "<tr>";
    				echo "<td> $mat[1] </td>" ;
    				echo "<td> $mat[5] </td>" ;
    				echo "<td> $mat[2] </td>" ;
                    echo "<td> $mat[3] </td>" ;
                    echo "<td> $mat[7] </td>" ;
                    echo "<td>  <a href='detalle.php?id=".$mat[0]."' class=''> <span class='glyphicon glyphicon-plus-sign' aria-hidden='true'></span> detalle </a> </td></tr>" ;
    			                                
    		}
    		mysqli_close($bd);
    		echo "</tbody></table>";
	?>
        </div>
    </body>
    <script type="text/javascript">
            $(document).ready(function(){
                $('#example').DataTable();
            });
    </script>
</html>
