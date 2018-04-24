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
            <h1>Adicionar Empleados</h1>
            <hr>
            <div class="col-sm-6">
                <form id="frm1" method="post" action="agregarbd.php" class="form form-horizontal">
            		<label>Cedula</label>
                            <input type="number" id="txtced" name="txtced" required min="1" class="form-control">
            		<label>Nombre</label>
            		<input type="text" id="txtnom" name="txtnom" maxlength="30" required class="form-control">
            		
            		<label>Cargo</label>
            		<select id="lstcar" name="lstcar" class="form-control">
            			<?php
            				include("../recursos/coneccion.php");
            				$bd = conectar();
            				if (!$bd) return;
            				$sql = "select * from cargos order by nombre";
            				$res = mysqli_query($bd,$sql);
            				while($arr=mysqli_fetch_array($res)){
            					echo "<option value='$arr[1]'>$arr[0]</option>";
            				}
            				mysqli_close($bd);
            			?>	
            		</select>
                            
        
            		<br>
                    <hr>
                    <input type="submit" class="btn-primary btn-sm" value="Guardar">
            </form>
            </div>
        </div>
    </body>
</html>
