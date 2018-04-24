<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Ejemplo basico BD</title>
        <link href="css/bootstrap.css" rel="stylesheet">
        <link href="css/estilo.css" rel="stylesheet">
        <script src="js/jquery.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container">
            <?php
                include ("./recursos/dibujaMenu.php");
            ?>
            <div class="jumbotron">
                <h1>Manejo de Bases de datos</h1>
                <p>Acceso a una base de datos denominada empresa, contiene los scripts básicos de gestión de tablas usando php.
                    Tiene solo dos tablas cargos(`codcar`, `nomcar`, `depend`) y 
                    empleados(`cedemp`, `nomemp`, `numofi`, `codcar`, `telofi`, `exteofi`) .Desarrollado por Luis Obeymar Estrada </p>
                <hr>
                <a href="empleados/lstEmpleados.php" class="btn-primary btn-lg">Ver Empleados</a>
                <a href="cargos/lstCargos.php" class="btn-primary btn-lg">Ver Cargos</a>
                <a href="recursos/empresa.txt" target="_blank" class="btn-success btn-lg">Ver Script BD</a>
            </div>
        </div>
    </body>
</html>
