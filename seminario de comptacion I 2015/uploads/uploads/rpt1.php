<?php
    include './fpdf/fpdf.php';
    $doc = new FPDF("P", "mm", "Letter");
    $doc->AddPage();
    
    $doc->SetFont("times", "I", 16);
    $doc->Cell(50, 10, "Hola Mundo", 1, 1);
    
    $doc->SetFont("arial", "", 9);
    $doc->Cell(50, 10, "Reporte PDF", 0, 1);
    
    $doc->Output();