<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style>
            table{
                border-style: solid;

            }
            td{
                border-style: solid;
            }
        </style>
    </head>
    <body>
        <?php
        $pre = $_POST["txtpre"];
        $int = $_POST["txtint"];
        $per = $_POST["optper"];
        $string = "<table><tr><td>cuota</td><td>valor cuota</td><td>saldo</td></tr>";
        echo "<h1>La cuota queda en:</h1>";
        $cuota =((pow(1+$int,$per)*$int)/(pow(1+$int,$per)-1))*$pre;
        $cuota = round($cuota,2);
        $saldo=$cuota*$per;
        for($x=0 ; $x<=$per ; $x++){

            $saldoo=$saldo-($cuota*$x);
            $string=$string."<tr><td>".$x."</td><td>".$cuota."</td><td>".$saldoo."</td></tr>";

        }
        $string=$string."</table>";

         echo $string ;
        
        ?>
    </body>
</html>
