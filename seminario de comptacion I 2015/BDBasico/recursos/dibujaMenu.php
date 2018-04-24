<?php
    $ruta = "http://localhost/BDBasico/";
    echo "<nav class='navbar navbar-default'>
           <div class='container-fluid'>
            <div class='navbar-header'>
              <button type='button' class='navbar-toggle collapsed' data-toggle='collapse' data-target='#bs-example-navbar-collapse-1' aria-expanded='false'>
                <span class='sr-only'>Toggle navigation</span>
                <span class='icon-bar'></span>
                <span class='icon-bar'></span>
                <span class='icon-bar'></span>
              </button>
              <a class='navbar-brand' href='#'>Manejo Base de datos</a>
            </div>

            <div class='collapse navbar-collapse' id='bs-example-navbar-collapse-1'>
              <ul class='nav navbar-nav'>
                  <li><a href='".$ruta."index.php'><span class='glyphicon glyphicon-home' aria-hidden='true'></span> Inicio</a></li>
            <li class='dropdown'>
                      <a href='#' class='dropdown-toggle' data-toggle='dropdown' role='button' aria-haspopup='true' aria-expanded='false'>
                      <span class='glyphicon glyphicon-calendar' aria-hidden='true'></span> Cargos <span class='caret'></span></a>
                      <ul class='dropdown-menu'>
                            <li><a href='".$ruta."cargos/addCargos1.php'><span class='glyphicon glyphicon-plus' aria-hidden='true'></span> Adicionar</a></li>
                            <li><a href='".$ruta."cargos/eliCargos1.php'><span class='glyphicon glyphicon-trash' aria-hidden='true'></span> Eliminar</a></li>
                            <li role='separator' class='divider'></li>
                            <li><a href='".$ruta."cargos/lstCargos.php'><span class='glyphicon glyphicon-th' aria-hidden='true'></span> Listar</a></li>
                      </ul>
            </li>

            <li class='dropdown'>
                      <a href='#' class='dropdown-toggle' data-toggle='dropdown' role='button' aria-haspopup='true' aria-expanded='false'>
                      <span class='glyphicon glyphicon-user' aria-hidden='true'></span> Empleados <span class='caret'></span></a>
                      <ul class='dropdown-menu'>
                            <li><a href='".$ruta."empleados/addEmpleados1.php'><span class='glyphicon glyphicon-plus' aria-hidden='true'></span> Adicionar</a></li>
                            <li><a href='".$ruta."empleados/eliEmpleados1.php'><span class='glyphicon glyphicon-trash' aria-hidden='true'></span> Eliminar</a></li>
                            <li><a href='".$ruta."empleados/modEmpleados1.php'><span class='glyphicon glyphicon-pencil' aria-hidden='true'></span> Modificar</a></li>
                            <li role='separator' class='divider'></li>
                            <li><a href='".$ruta."empleados/lstEmpleados.php'><span class='glyphicon glyphicon-th' aria-hidden='true'></span> Listar</a></li>
                      </ul>
            </li>            
            </ul>
            </div>
           </div>
           </nav>
";
?>
