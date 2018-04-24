<?php
    include './fpdf/fpdf.php';
    
    class PDF extends FPDF{
        function Header() {
            $this->Image("logo.jpg", 10, 10, 10);
            $this->SetFont("Arial", "B", 16);
            $this->SetTextColor(0, 0, 250);
            $this->Cell(0, 10, "Reporte de prueba", 0, 0, "C");
            $this->Ln(16);
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
    $doc->SetFont("Arial", "", 10);
    $doc->Cell(0, 10, "tabla de 7", 0, 1);
    $doc->Ln(3);
    $r=0;
    $i=0;
    for($i=1;$i<=200;$i++){
        $r=7*$i;
        $doc->Cell(40, 10, "7 X $i = $r", 0, 1);
    }
    
    $doc->Output();