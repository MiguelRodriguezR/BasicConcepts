<?php echo form_open();?>

<?php
if(form_error()){
  echo "
  <script type='text/javascript'>
      $(document).ready(function(){

          $.notify({
              icon: 'pe-7s-like2',
              message: 'complete todos los campos'

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
                        <h4 class="title">Agregar Usuario</h4>
                    </div>
                    <div class="content">

                            <div class="row">
                                <div class="col-md-5">
                                    <div class="form-group">
                                        <label>Tipo</label>
                                        <select name="tipo">
                                          <option value="docente">docente</option>
                                          <option value="administrador">administrador</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-md-3">
                                    <div class="form-group">
                                        <label>Cedula</label>
                                        <input name="cedula" type="text" class="form-control"   placeholder="" value="">
                                    </div>
                                </div>
                            </div>

                            <div class="row">
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label>Nombre</label>
                                        <input type="text" class="form-control" name="nombre" placeholder="" value="">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label>Apellido</label>
                                        <input type="text" class="form-control" name="apellido" placeholder="" value="">
                                    </div>
                                </div>
                            </div>





                            <div class="clearfix"></div>
                        </form>
                    </div>
                    <button type="submit" class="btn btn-info btn-fill pull-left">Agregar Usuario</button>
                </div>
            </div>




        </div>
    </div>
</div>
