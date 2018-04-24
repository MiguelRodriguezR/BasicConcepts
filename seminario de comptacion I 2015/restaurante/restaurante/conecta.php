<?php
    function conectar(){
        $bd = mysqli_connect("localhost","root","","restaurante");
        if (!$bd){
            echo "<h3>Error de conexion</h3>";
            return null;
        }     
        return $bd;
    }

?>


