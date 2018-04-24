<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Lista de clientes</title>
    </head>
    <body>
        <h1>Lista de clientes</h1>
        <?php
            include './conecta.php';
            $bd = conectar();
            $sql = "select * from cliente order by nombre";
            $res = mysqli_query($bd,$sql);//dispara esta consulta en esta base de datos
            while ($arr = mysqli_fetch_array($res)){
                echo "<br>" . utf8_encode($arr[1]);
                                
            }
            mysqli_close($bd);
        ?>
    </body>
</html>
