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
                $id = $_GET['id'];
        		
		
        		
        		include("../recursos/coneccion.php");
        		$bd = conectar();
        		if (!$bd) return;

                echo "<h1> Detalles de tiquetera </h1>" ;
                $tipo=0;
                $consumo=0;
                $tamano=0;
                $sql="SELECT * FROM tiqueteras,tipos WHERE tipos.id = tiqueteras.tipo and tiqueteras.id = $id";
                echo "<table class='table table-striped'>";
                echo "<tr><th>Cliente</th> <th>Cedula</th> <th>Tamaño</th> <th>Consumo</th> <th>Tipo</th> </tr>";
                $res = mysqli_query($bd,$sql);
                while($mat = mysqli_fetch_array($res)){
                        echo "<tr>";
                        echo "<td> $mat[1] </td>" ;
                        echo "<td> $mat[5] </td>" ;
                        echo "<td> $mat[2] </td>" ;
                        echo "<td> $mat[3] </td>" ;
                        echo "<td> $mat[7] </td>" ;
                        $tamano=$mat[2];
                        $consumo=$mat[3];
                        $tipo=$mat[4];
                                                    
                }

                mysqli_close($bd);
                echo "</table>";

                $bd = conectar();
                if (!$bd) return;

                echo "<h1> Consumos </h1>" ;
             
                $sql="SELECT * FROM consumos,platos WHERE  platos.id = consumos.plato ";
                echo "<table class='table table-striped'>";
                echo "<tr><th>Plato</th> <th>Fecha</th> </tr>";
                $res = mysqli_query($bd,$sql);
                while($mat = mysqli_fetch_array($res)){

                    if($id==$mat[3]){
                            
                            echo "<tr>";
                            echo "<td> $mat[5] </td>" ;
                            echo "<td> $mat[2] </td>" ;
                        }                     
                                                    
                }
                mysqli_close($bd);
                if($consumo<$tamano){
                echo "</table>";
                    echo '<form id="frm1" method="post" action="agregarplato.php?id='.$id.'" class="form form-horizontal">';
                    echo "<label>Plato</label><select id='lstcar' name='lstplatos' class='form-control'>";
                                $bd = conectar();
                                if (!$bd) return;
                                $sql = 'SELECT * FROM platos  ';
                                $res = mysqli_query($bd,$sql);
                                //echo mysqli_fetch_array($res);
                                while($arr=mysqli_fetch_array($res)){
                                    if($arr[2]==$tipo){
                                        echo "<option value='$arr[0]'>$arr[1] </option>";
                                    }
                                }
                                mysqli_close($bd);
                    echo "</select>";

                    echo '<input type="submit" class="btn-primary btn-sm" value="Consumir">';
                }
                else{
                    echo "<div class='alert alert-danger' role='alert'><strong>Consumo completo</strong> Esta tiquetera ha sido consumida completamente";
                }

		
            ?>
        </div>
    </body>
</html>