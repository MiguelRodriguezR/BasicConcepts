<?php echo form_open_multipart('inicio/agregar_productividad');?>

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
                        <h4 class="title">Agregar Productividad</h4>
                    </div>
                    <div class="content">

                            <div class="row">
                                <div class="col-md-5">
                                    <div class="form-group">
                                        <label>Tipo</label>
                                        <input name="tipo" type="text" class="form-control"   placeholder="" value="">
                                    </div>
                                </div>
                                <div class="col-md-5">
                                  <div class="form-group">
                                      <label>Titulo</label>
                                      <input name="titulo" type="text" class="form-control"   placeholder="" value="">
                                  </div>

                                </div>
                            </div>

                            <div class="row">
                                <div class="col-md-3">
                                    <div class="form-group">
                                        <label>Fecha de Realizacion</label>
                                        <input
                                            id="input_01"
                                            class="datepicker"
                                            name="fecha_r"
                                            type="text"
                                            autofocuss
                                            value=""
                                            data-valuee="">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                  <div class="form-group">

                                      <label>Lugar de desarrollo</label>
                                      <input name="lugar" type="text" class="form-control"   placeholder="" value="">
                                  </div>
                                </div>
                            </div>

                            <div class="row">
                                <div class="col-md-3">
                                    <div class="form-group">
                                        <label>descripcion</label>
                                        <input name="descripcion" type="text" class="form-control"   placeholder="" value="">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                  <div class="form-group">

                                      <label>certificado</label>
                                    <input id="imagen" name="certificado" type="file" class="file" accept=".pdf">
                                  </div>
                                </div>
                            </div>





                            <div class="clearfix"></div>
                        </form>
                    </div>
                    <button type="submit" class="btn btn-info btn-fill pull-left">Agregar Productividad</button>
                </div>
            </div>




        </div>
    </div>
</div>
<script type="text/javascript">

    var $input = $( '.datepicker' ).pickadate({
        formatSubmit: 'yyyy/mm/dd',
        format: 'yyyy-mm-dd',
        // min: [2015, 7, 14],
        //container: '#container',
        //editable: true
        //closeOnSelect: false,
        //closeOnClear: false,
    })

    //var picker = $input.pickadate('picker')
    // picker.set('select', '14 October, 2014')
    // picker.open()

    // $('button').on('click', function() {
    //     picker.set('disable', true);
    // });

</script>
