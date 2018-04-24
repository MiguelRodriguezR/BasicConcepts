<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Resultado</h1>
        <?php
            include './conecta.php';
            $bd = conectar();
            if (!$bd) return;
            
            $a = $_POST["t1"];
            $b = $_POST["t2"];
            $c = $_POST["t3"];
            
            $sql = "insert into cargos values('$a','$b','$c')";
            $result = mysqli_query($bd, $sql);
            if ($result){
                
                echo "<div class='alert alert-success' role='alert'>Registro adicionado con exito</div>";
            }
            else{
                echo "<div class='alert alert-danger' role='alert'>";
                echo "<b>Error:</b>";
                echo mysqli_error($bd) . "</div>";
            }
            mysqli_close($bd);
            
        ?>
    </body>
</html>
