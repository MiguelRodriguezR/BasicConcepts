<?php
    function conectar(){
        $bd = mysqli_connect("localhost","root","","empresa"); //conectarse con mysql
        if (!$bd){
            echo"<h3>Error de conexón</h3>"; // si nomostrar error de conexion
            echo mysqli_errno($bd);
            return NULL;
        }
        //como el la version 7 de php ya selecciono la base de datos lo siguiente sobra
        /*if (!mysql_select_db("restaurante",$bd)){ //si no conecta con la base de datos
            echo "<h3>Error: BD no existe</h3>";
            return null;
        }
         */ 
         
        return $bd;
    }
?>