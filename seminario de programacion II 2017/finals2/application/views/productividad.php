<div class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="header">
                        <h4 class="title">Tabla de Productividad</h4>
                        <p class="category">todos los libros que has publicado y eventos en los que has participado</p>
                    </div>
                    <div class="content table-responsive table-full-width">
                        <table class="table table-hover table-striped">
                          <thead>
                            <th>Titulo</th>
                            <th>Tipo</th>
                            <th>Fecha de realizacion</th>
                            <th>Lugar de Desarrollo</th>
                            <th>Descripcion</th>
                            <th>Certificado/Documento</th>
                          </thead>
                          <tbody>
                          <?php
                            foreach ($respuesta as $res){
                              echo'
                              <tr>
                                <td>'.$res->titulo.'</td>
                                <td>'.$res->tipo.'</td>
                                <td>'.$res->fecha_realizacion.'</td>
                                <td>'.$res->lugar_desarrollo.'</td>
                                <td>'.$res->descripcion.'</td>
                                <td><a target="_blank" href="'.base_url()."static/datos/".$res->certificado.'.pdf">'.$res->certificado.'</a></td>
                              </tr>
                              ';
                            }

                          ?>
                          </tbody>

                        </table>


                    </div>

                </div>
                <a href="<?php echo base_url(); ?>inicio/agregar_productividad" class="btn btn-info btn-fill pull-left"><i class="pe-7s-add-user"></i> Agregar Productividad</a>

            </div>




        </div>
    </div>
</div>
