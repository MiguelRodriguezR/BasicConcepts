<div class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="header">
                        <h4 class="title">Tabla de Estudios</h4>
                        <p class="category">todos los estudios realizados por ti</p>
                    </div>
                    <div class="content table-responsive table-full-width">
                        <table class="table table-hover table-striped">
                          <thead>
                            <th>Titulo</th>
                            <th>Grado</th>
                            <th>Fecha de Grado</th>
                            <th>Modalidad</th>
                          </thead>
                          <tbody>
                          <?php
                            foreach ($respuesta as $res){
                              echo'
                              <tr>
                                <td>'.$res->titulo.'</td>
                                <td>'.$res->grado.'</td>
                                <td>'.$res->fecha_grado.'</td>
                                <td>'.$res->modalidad.'</td>
                              </tr>
                              ';
                            }

                          ?>
                          </tbody>

                        </table>


                    </div>

                </div>
                <a href="<?php echo base_url(); ?>inicio/agregar_est" class="btn btn-info btn-fill pull-left"><i class="pe-7s-add-user"></i> Agregar Estudio</a>

            </div>




        </div>
    </div>
</div>
