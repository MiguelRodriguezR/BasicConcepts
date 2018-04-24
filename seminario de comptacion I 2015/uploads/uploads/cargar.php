<html>
    <head>
        <meta charset="UTF-8">
        <title>Cargar Archivos</title>
    </head>
    <body>
        <h1>Resultado de la carga</h1>
        <?php
            // put your code here
            $des = $_POST["txtdes"];
            echo "<h3>Descripcion</h3>$des<br>";
            
            $tmp = $_FILES["txtarc"]["tmp_name"];
            $nom = $_FILES["txtarc"]["name"];
            $tam = $_FILES["txtarc"]["size"];
            $err = $_FILES["txtarc"]["error"];
            if ($err==0){
                echo "El archivo $nom llego correctamente";
                echo "<br>Nombre temporal: $tmp";
                echo "<br>Tamaño: $tam bytes";
                
                move_uploaded_file($tmp, "recursos/$nom");
                echo "<br><a href='recursos/$nom' target='_blank'>Ver</a>";//hipervinculo para ver o descargar
            }
            else{
                echo "<h3>Error</h3>El archivo no llegó";
            }
        ?>
    </body>
</html>
