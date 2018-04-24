<?php 
        include ("recursos/conecta.php");
        $bd = conectar();
        if (!$bd) return;
        $id = $_POST["id"];
        $cargo = $_POST["cargo"];
        $nombre = $_POST["nombre"];
        $apellido = $_POST["apellido"];
        $sql = "INSERT into aspirantes (cedula,nombre,apellido,cargo) values ( '$id' , '$nombre', '$apellido' , '$cargo')";
        $res = mysqli_query($bd,$sql);
        if ($res==1) {
            echo "<div class='alert alert-success' role='alert'><strong>Atención</strong> Registro adicionado con éxito</div>";
        }
        else {
            echo "<div class='alert alert-danger' role='alert'><strong>Error</strong> Registro NO adicionado";
            echo " - " .  mysqli_error($bd)  . "</div>";
        }


?>