<?php echo form_open_multipart('inicio/perfil');?>

<?php
  if($error!=""){
    foreach ($error as $item ){
        echo "
        <script type='text/javascript'>
            $(document).ready(function(){

                $.notify({
                    icon: 'pe-7s-door-lock',
                    message: '".$item."'

                  },{
                      type: 'danger',
                      timer: 4000,
                      placement: {
                            from: 'bottom',
                            align: 'left'
                        }
                  });

            });
        </script>

        ";
    }
  }
  if($exito!=""){
    echo "
    <script type='text/javascript'>
        $(document).ready(function(){

            $.notify({
                icon: 'pe-7s-like2',
                message: '".$exito."'

              },{
                  type: 'info',
                  timer: 4000,
                  placement: {
                      from: 'bottom',
                      align: 'left'
                  }
              });

        });
    </script>

    ";
  }
?>
<div class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-8">
                <div class="card">
                    <div class="header">
                        <h4 class="title">Editar Perfil</h4>
                    </div>
                    <div class="content">

                            <div class="row">
                                <div class="col-md-5">
                                    <div class="form-group">
                                        <label>Tipo</label>
                                        <input type="text" class="form-control" disabled placeholder="" value="<?php echo $this->session->tipo ?>.">
                                    </div>
                                </div>
                                <div class="col-md-3">
                                    <div class="form-group">
                                        <label>Cedula</label>
                                        <input type="text" class="form-control"  disabled placeholder="" value="<?php echo $this->session->cedula ?>">
                                    </div>
                                </div>
                            </div>

                            <div class="row">
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label>Nombre</label>
                                        <input type="text" class="form-control" name="nombre" placeholder="" value="<?php echo $this->session->nombre ?>">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label>Apellido</label>
                                        <input type="text" class="form-control" name="apellido" placeholder="" value="<?php echo $this->session->apellido ?>">
                                    </div>
                                </div>
                            </div>

                            <div class="row">
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label>Contreseña Antigua</label>
                                        <input type="text" class="form-control" name="clave_a" placeholder="" value="">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label>Nueva Contraseña</label>
                                        <input type="text" class="form-control" name="clave_n" placeholder="" value="">
                                    </div>
                                </div>
                            </div>




                            <div class="clearfix"></div>
                        </form>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card card-user">
                    <div class="image">
                        <img src="<?php echo base_url(); ?>static/light/assets/img/sidebar-5.jpg" alt="..."/>
                    </div>
                    <div class="content">
                        <div class="author">
                             <a href="#">
                            <img class="avatar border-gray" src="<?php echo base_url(); ?>static/imagenes/<?php echo $this->session->img?>.jpg" alt="..."/>

                              <h4 class="title">Foto de perfil<br />

                              </h4>
                            </a>
                        </div>
                        <input id="imagen" name="img" type="file" class="file" accept=".jpg">

                    </div>
                    <hr>
                </div>
                <button type="submit" class="btn btn-info btn-fill pull-right">Actualizar perfil</button>
            </div>



        </div>
    </div>
</div>
