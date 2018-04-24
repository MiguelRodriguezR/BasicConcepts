<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Resultado</h1>
        <?php
        // put your code here
        include './conecta.php';
        $bd = conectar();
        $op1 = $_GET["op1"];
        $sql = "delete from cliente where id_cli='$op1'";
        $res = mysqli_query($bd,$sql);
        if ($res){
            echo "Registro eliminado";
            //header("Location:index.php");
        }
        else echo "Error: " . mysqli_error($bd);
mysqli_close($bd)
        ?>
        <a href="index.php">Inicio</a>
    </body>
</html>
