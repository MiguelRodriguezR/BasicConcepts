<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        
    </head>
    <body>
        
        <div class="col-sm-7">
            <h1>Lista de cargos</h1>
        <?php
            include './conecta.php';
            $bd = conectar();
            if (!$bd) return;
            $sql = "select nomcar, count(nomemp), cargos.codcar as cuenta from empleados, cargos where cargos.codcar = empleados.codcar group by nomcar order by cuenta desc limit 20;";
            echo "<div class='list-group'>";
            $result = mysqli_query($bd, $sql);
            while ($arr = mysqli_fetch_array($result)){
                echo "<a href='#' class='list-group-item' onclick=llamar('" . $arr[2] . "');>";
                echo "<span class='badge'>$arr[1]</span>";
                echo "$arr[0]</a>";
            }
            echo "</div>";
            mysqli_close($bd);
        ?>
        </div>
        <div class="col-sm-5">
            <h1>Lista de empleados</h1>
            <div id="divres1"></div>
        </div>
    </body>
</html>
