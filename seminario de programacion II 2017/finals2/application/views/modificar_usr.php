<?php echo form_open();?>

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
                                        <input type="text" class="form-control" disabled placeholder="" value="<?php echo $this->session->tipou ?>.">
                                    </div>
                                </div>
                                <div class="col-md-3">
                                    <div class="form-group">
                                        <label>Cedula</label>
                                        <input type="text" class="form-control"  disabled placeholder="" value="<?php echo $this->session->cedulau ?>">
                                    </div>
                                </div>
                            </div>

                            <div class="row">
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label>Nombre</label>
                                        <input type="text" class="form-control" name="nombre" placeholder="" value="<?php echo $this->session->nombreu ?>">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label>Apellido</label>
                                        <input type="text" class="form-control" name="apellido" placeholder="" value="<?php echo $this->session->apellidou ?>">
                                    </div>
                                </div>
                            </div>

                            <div class="row">
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
                <button type="submit" class="btn btn-info btn-fill pull-left">Actualizar usuario</button>
            </div>




        </div>
    </div>
</div>
