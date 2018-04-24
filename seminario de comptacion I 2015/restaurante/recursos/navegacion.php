<?php
  $ruta = "http://localhost/restaurante/";
  echo '<nav class="navbar navbar-default">
          <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="'.$ruta.'index.php">Restaurante Don Pepe</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
              <ul class="nav navbar-nav">
              <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Empleados <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="'.$ruta.'empleados/agregar.php"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Agregar</a></li>
                    <li><a href="'.$ruta.'empleados/eliminar.php"><span class="glyphicon glyphicon-minus" aria-hidden="true"></span> Eliminar</a></li>
                 
                    <li role="separator" class="divider"></li>
                    <li><a href="'.$ruta.'empleados/listar.php"><span class="glyphicon glyphicon-th-large" aria-hidden="true"></span> Listar</a></li>
                  </ul>
                </li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Tiqueteras <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                     <li><a href="'.$ruta.'tiqueteras/agregar.php"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Agregar</a></li>
              
                
                    <li role="separator" class="divider"></li>
                    <li><a href="'.$ruta.'tiqueteras/listar.php"><span class="glyphicon glyphicon-th-large" aria-hidden="true"></span> Listar</a></li>
                  </ul>
                </li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Platos <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="'.$ruta.'platos/agregar.php"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Agregar</a></li>
                    <li><a href="'.$ruta.'platos/eliminar.php"><span class="glyphicon glyphicon-minus" aria-hidden="true"></span> Eliminar</a></li>
    
                    <li role="separator" class="divider"></li>
                    <li><a href="'.$ruta.'platos/listar.php"><span class="glyphicon glyphicon-th-large" aria-hidden="true"></span> Listar</a></li>
                  </ul>
                </li>
              </ul>
            </div><!-- /.navbar-collapse -->
          </div><!-- /.container-fluid -->
      </nav>';

?>