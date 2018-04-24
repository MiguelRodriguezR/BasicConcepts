<?php
    function conectar(){
        $bd = mysqli_connect("localhost","root","","empresa");
        if (!$bd){
            echo "<h3>Error de conexión</h3>";
            return null;
        }
        return $bd;
    }
?>

