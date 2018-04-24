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
            <h1>Adicionar Cargos</h1>
            <hr>
            <div class="col-sm-6">
            <form id="frm1" method="post" action="addCargos2.php" class="form form-horizontal">
			<label>Codigo</label>
                        <input type="number" min="1" max="999" id="txtcod" name="txtcod"  required class="form-control" >
                        
			<label>Nombre</label>
                        <input type="text" id="txtnom" name="txtnom"  required class="form-control">
			
                        <label>Dependencia</label>
			<select id="lstdep" name="lstdep" class="form-control">
				<option>General</option>
				<option>Sistemas</option>
				<option>Ventas</option>
				<option>Pagos</option>
			</select>
                        <hr>
                        <input type="submit" class="btn-primary btn-sm" value="Guardar">
            </form>
            </div>
        </div>
    </body>
</html>
