<?php
    include './fpdf/fpdf.php';
    
    class PDF extends FPDF{
        function Header() {
            $this->Image("logo.jpg", 10, 10, 10);
            $this->SetFont("Arial", "B", 16);
            $this->SetTextColor(0, 0, 250);
            $this->Cell(0, 10, "Empresa ABC", 0, 1, "C");
            $this->SetTextColor(0, 0, 0);
            $this->SetFont("Arial", "", 14);
            $this->Cell(0, 10, "Reporte de Empleados", 0, 0, "C");
            $this->Ln(20);
        }
        function Footer() {
            $this->SetY(-15);
            $this->SetFont("Arial", "I", 9);
            $this->Cell(0, 10, "Pagina" . $this->PageNo()."de {nb}", 0, 0, "C");
        }
    }

    $doc = new PDF();
    $doc->AliasNbPages();
    $doc->AddPage();
    $doc->SetFont("Arial", "B", 10);
    $doc->Ln(3);
    
    $doc->SetTextColor(0, 100, 200);
    $doc->Cell(20, 10, "Cedula", 1, 0, "C");
    $doc->Cell(40, 10, "Nombre", 1, 0, "C");
    $doc->Cell(20, 10, "Telefono", 1, 1, "C");
    
    $doc->SetTextColor(0, 0, 0);
    include './conecta.php';
    $bd= conectar();
    if(!$bd){
        $doc->Cell(20, 10, "No hay acceso a la base de datos", 1, 1, "C");
    }
    else{
        $query="select cedemp, nomemp,telofi from empleados order by nomemp";
        $result= mysqli_query($bd, $query);
        while($arr= mysqli_fetch_array($result)){
            $doc->Cell(20, 10, $arr[0], 1, 0);
            $doc->Cell(40, 10, $arr[1], 1, 0);
            $doc->Cell(20, 10, $arr[2], 1, 1);
        }
        mysqli_close($bd);
    }
    
    $doc->Output();