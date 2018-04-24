<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Resultado</h1>
        <?php
            include './conecta.php';
            $bd = conectar();
            $id = $_POST["txt_id"];
            $nom = utf8_decode($_POST["txtnom"]);
            $dir = utf8_decode($_POST["txtdir"]);
            $tel = $_POST["txttel"];
            $sql = "insert into cliente values('$id','$nom','$dir','$tel')";
            $res = mysqli_query($bd,$sql);
            if (!$res){
                echo "Error: " . mysqli_error($bd);
            }
            else{
                echo "Registro adicionado";
            }
        ?>
        
    </body>
</html>
