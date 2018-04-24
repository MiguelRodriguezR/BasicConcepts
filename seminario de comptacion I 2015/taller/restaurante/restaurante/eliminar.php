<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Eliminar cliente</title>
    </head>
    <body>
        <h1>Eliminar cliente</h1>
        <form method="get" action="eliminar2.php">
           
        
        <?php
            include './conecta.php';
            $bd = conectar();
            $sql = "select * from cliente order by nombre";
            $res = mysqli_query($bd, $sql);
            while ($arr = mysqli_fetch_array($res)){
                echo "<br>";
                echo "<input type='radio' value = '$arr[0]' name='op1'>";
                echo " " . utf8_encode($arr[1]);
            }
            mysqli_close($bd);
        ?>
            <hr><input type="submit" value="Eliminar">
    </form>
    </body>
</html>
