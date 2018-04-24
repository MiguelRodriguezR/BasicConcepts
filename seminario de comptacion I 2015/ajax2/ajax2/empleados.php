<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <br>
        <h3>Lista de empleados</h3>
        <div class="col-sm-5">
        <ul class="list-group">
        <?php
            include './conecta.php';
            $bd = conectar();
            if (!$bd) return;
            $sql = "select nomemp from empleados";
            $result = mysqli_query($bd, $sql);
            while ($arr = mysqli_fetch_array($result)){
                echo "<li class='list-group-item'>$arr[0]</li>";
            }
            mysqli_close($bd);
        ?>
        </ul>
        </div>
    </body>
</html>
