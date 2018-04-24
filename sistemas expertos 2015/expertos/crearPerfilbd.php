<?php 
        include ("recursos/conecta.php");
        $bd = conectar();
        if (!$bd) return;
        $id = $_POST["id"];
        $cargo = $_POST["cargo"];
        $porcentaje = $_POST["porcentaje"];
        $sql = "INSERT into perfil (cargo,minima,id) values ( '$cargo' , '$porcentaje', '$id')";
        $res = mysqli_query($bd,$sql);
        if ($res==1) {
            echo "<div class='alert alert-success' role='alert'><strong>Atención</strong> Registro adicionado con éxito</div>";
        }
        else {
            echo "<div class='alert alert-danger' role='alert'><strong>Error</strong> Registro NO adicionado";
            echo " - " .  mysqli_error($bd)  . "</div>";
        }


?>