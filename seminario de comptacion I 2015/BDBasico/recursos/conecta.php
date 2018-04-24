<?php
    function conectar(){
        $bd = mysqli_connect("localhost", "root", "", "empresa");
        if (!$bd){
            echo "<h2>Error al conectar a la base de datos</h2>";
            echo "<hr>" . mysqli_error($bd);
            return null;
        }
        return $bd;
    }
?>