<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Carga de Archivos</title>
    </head>
    <body>
        <h1>Cargar archivos al servidor</h1>
        <form method="post" action="cargar.php" enctype="multipart/form-data">
            <label>Descripcion del archivo</label>
            <br>
            <textarea name="txtdes"></textarea>
            <br>
            <label>Seleccione el archivo</label>
            <input type="file" name="txtarc">
            <hr>
            <input type="submit" value="Enviar">
        </form>
        <h1>REPORTES</h1>
        <a href="rpt1.php">Reporte 1 </a>
        <a href="rpt2.php">Reporte 2 </a>
        <a href="rpt3.php">Reporte 3 </a>
        
    </body>
</html>
