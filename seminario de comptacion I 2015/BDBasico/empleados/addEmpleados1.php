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
            <h1>Adicionar Empleados</h1>
            <hr>
            <div class="col-sm-6">
                <form id="frm1" method="post" action="addEmpleados2.php" class="form form-horizontal">
		<label>Cedula</label>
                <input type="number" id="txtced" name="txtced" required min="1" class="form-control">
		<label>Nombre</label>
		<input type="text" id="txtnom" name="txtnom" maxlength="30" required class="form-control">
		<label>Número de Oficina</label>
		<select id="lstofi" name="lstofi" class="form-control">
			<option>101</option>	<option>201</option>	<option>301</option>	<option>401</option>
		</select>
		
		<label>Cargos</label>
		<select id="lstcar" name="lstcar" class="form-control">
			<?php
				include("../recursos/conecta.php");
				$bd = conectar();
				if (!$bd) return;
				$sql = "select * from cargos order by nomcar";
				$res = mysqli_query($bd,$sql);
				while($arr=mysqli_fetch_array($res)){
					echo "<option value='$arr[0]'>$arr[1]</option>";
				}
				mysqli_close($bd);
			?>	
		</select>
                
		<label>Teléfono</label>
		<input type="number" id="txttel" name="txttel" required min="0" class="form-control"><br>
                
		<label>Extensión</label>
		<input type="number" id="txtext" name="txtext" required min="0" max="999"  class="form-control" /><br>
                <hr>
                <input type="submit" class="btn-primary btn-sm" value="Guardar">
            </form>
            </div>
        </div>
    </body>
</html>
