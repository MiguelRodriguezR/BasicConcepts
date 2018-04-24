<div class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="header">
                        <h4 class="title">Tabla de Usuarios</h4>
                        <p class="category">todos los usuarios disponibles en esta institucion</p>
                    </div>
                    <div class="content table-responsive table-full-width">
                        <table class="table table-hover table-striped">
                          <thead>
                            <th>Cedula</th>
                            <th>Nombre</th>
                            <th>Apellido</th>
                            <th>Tipo</th>
                            <th>Modificar</th>
                            <th>Eliminar</th>
                          </thead>
                          <tbody>
                          <?php
                            foreach ($respuesta as $res){
                              echo'
                              <tr>
                                <td>'.$res->cedula.'</td>
                                <td>'.$res->nombre.'</td>
                                <td>'.$res->apellido.'</td>
                                <td>'.$res->tipo.'</td>
                                <td>
                                    <a href="'.base_url().'inicio/modificar_usr/'.$res->cedula.'"><i class="pe-7s-note"></i>modificar</a>
                                </td>
                                <td>
                                    <a href="'.base_url().'inicio/eliminar_usr/'.$res->cedula.'"><i class="pe-7s-delete-user"></i> eliminar</a>
                                </td>
                              </tr>
                              ';
                            }

                          ?>
                          </tbody>

                        </table>


                    </div>

                </div>
                <a href="<?php echo base_url(); ?>inicio/agregar_usr" class="btn btn-info btn-fill pull-left"><i class="pe-7s-add-user"></i> Agregar Usuario</a>

            </div>




        </div>
    </div>
</div>
