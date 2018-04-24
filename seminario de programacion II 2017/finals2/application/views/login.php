<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Log In</title>

    <!--   Core JS Files   -->
    <script src="<?php echo base_url(); ?>static/light/assets/js/jquery.3.2.1.min.js" type="text/javascript"></script>
    <script src="<?php echo base_url(); ?>static/light/assets/js/bootstrap.min.js" type="text/javascript"></script>

    <!--  Notifications Plugin    -->
    <script src="<?php echo base_url(); ?>static/light/assets/js/bootstrap-notify.js"></script>


    <link rel="shortcut icon" type="image/png" href="<?php echo base_url(); ?>static/imagenes/udenar.png  "/>


    <!-- Bootstrap core CSS     -->
    <link href="<?php echo base_url(); ?>static/light/assets/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Animation library for notifications   -->
    <link href="<?php echo base_url(); ?>static/light/assets/css/animate.min.css" rel="stylesheet"/>

    <!--  Light Bootstrap Table core CSS    -->
    <link href="<?php echo base_url(); ?>static/light/assets/css/light-bootstrap-dashboard.css?v=1.4.0" rel="stylesheet"/>


    <link rel="stylesheet" href="<?php echo base_url(); ?>static/css/font-awesome.min.css">
    <link rel="stylesheet" href="<?php echo base_url(); ?>static/css/bulma.min.css"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=0">
    <link rel="stylesheet" href="<?php echo base_url(); ?>static/css/main.css">


    <script src="<?php echo base_url(); ?>static/js/particles.js"></script>
    <script src="<?php echo base_url(); ?>static/js/main.js"></script>


  </head>
  <body>

    <div class="columns is-vcentered">
      <div class="login column is-4 ">
        <section class="section">



          <?php echo form_open();?>
          <div class="field">
            <label class="label">Cedula</label>
            <div class="control has-icons-right">

              <input class="input" type="text" name="cedula">
              <span class="icon is-small is-right">
                <i class="fa fa-user"></i>
              </span>
            </div>
          </div>

          <div class="field">
            <label class="label">Contraseña</label>
            <div class="control has-icons-right">

              <input class="input" type="password" name="clave">
              <span class="icon is-small is-right">
                <i class="fa fa-key"></i>
              </span>
            </div>
          </div>

          <div class="field">
            <label class="label"></label>
            <div class="control has-icons-right">
              <div class="has-text-centered">
                <img class="login-logo" src="<?php echo base_url(); ?>static/captcha/<?php echo $this->session->captcha["id"]; ?>.jpg">
              </div>
              <input class="input" type="text" name="captcha">
              <span class="icon is-small is-right">
                <i class="fa fa-key"></i>
              </span>
            </div>
          </div>
          <div class="has-text-centered">
            <input type="submit" class="button is-vcentered is-dark is-outlined">
          </div>
          <div class="has-text-centered  is-dark">
            Por favor ingrese la palabra que se muestra en el recuadro

          </div>
        </section>
      </div>
      <div id="particles-js" class="interactive-bg column is-8">
      </div>
    </div>
    <?php
      if(form_error('cedula')){
        echo "
        <script type='text/javascript'>
            $(document).ready(function(){

                $.notify({
                    icon: 'pe-7s-door-lock',
                    message: '".form_error('cedula')."'

                  },{
                      type: 'danger',
                      timer: 4000
                  });

            });
        </script>

        ";
      }
    ?>
    <?php
      if(form_error('clave')){
        echo "
        <script type='text/javascript'>
            $(document).ready(function(){

                $.notify({
                    icon: 'pe-7s-door-lock',
                    message: '".form_error('clave')."'

                  },{
                      type: 'danger',
                      timer: 4000
                  });

            });
        </script>

        ";
      }
    ?>
    <?php
      if($error!="-1"){
        echo "
        <script type='text/javascript'>
            $(document).ready(function(){

                $.notify({
                    icon: 'pe-7s-door-lock',
                    message: '".$error."'

                  },{
                      type: 'danger',
                      timer: 4000
                  });

            });
        </script>

        ";
      }
    ?>
  </body>





</html>
