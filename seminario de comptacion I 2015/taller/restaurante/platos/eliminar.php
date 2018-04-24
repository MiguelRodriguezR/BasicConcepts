<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>restaurante</title>
        <link href="../css/bootstrap.css" rel="stylesheet">
        <link href="../css/estilo.css" rel="stylesheet">
        <script src="../js/jquery.js"></script>
        <script src="../js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container">
            <?php
                include ("../recursos/navegacion.php");
            ?>
            <h1>Eliminar Platos</h1>
            <hr>
            <div class="col-sm-5">
            <form action="eliminarbd.php" method="post">
            <?php
    include ("../recursos/coneccion.php");
    $bd = conectar();
    if (!$bd) return;
    $sql = "SELECT * from platos";
    echo "<table class='table table-striped'>";
    echo "<tr><th>Seleccione codigo plato</th> <th>Nombre del plato</th> </tr>";
    $res = mysqli_query($bd,$sql);
    while($mat = mysqli_fetch_array($res)){
        echo "<tr>";
        echo "<td> <input type='radio' name='victima' value='$mat[0]'> $mat[0]</td>";
        echo "<td> $mat[1] </td>" ;
        echo "</tr>" ;
    }
    mysqli_close($bd);
    echo "</table>";
            ?>
                <hr>
                <input type="submit" class="btn-danger btn-sm" value="Eliminar!">
            </form>
            </div>
        </div>
    </body>
</html>
