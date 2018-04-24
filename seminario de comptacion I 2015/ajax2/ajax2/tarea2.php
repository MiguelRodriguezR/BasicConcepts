<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <br>
        <ul class="list-group">
        <?php
            include './conecta.php';
            $bd = conectar();
            if (!$bd) return;
            $cod = $_GET["var"];
            $sql = "select nomemp from empleados natural join cargos where cargos.codcar='$cod'";
            //echo "$sql";
            $result = mysqli_query($bd, $sql);
            while ($arr = mysqli_fetch_array($result)){
                echo "<li class='list-group-item'>$arr[0]</li>";
            }
            mysqli_close($bd);
        ?>
        </ul>
        
    </body>
</html>
