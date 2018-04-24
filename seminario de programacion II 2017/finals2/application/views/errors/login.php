<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Login - Free Bulma template</title>
  <link rel="shortcut icon" type="image/png" href="<?php echo base_url(); ?>static/imagenes/udenar.png  "/>
  <link rel="stylesheet" href="<?php echo base_url(); ?>static/css/font-awesome.min.css">
  <link rel="stylesheet" href="<?php echo base_url(); ?>static/css/bulma.min.css">
</head>
<body>
  <section class="hero is-info is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="column is-4 is-offset-4">
          <h3 class="title has-text-white">Inicio de Sesion</h3>
          <p class="subtitle has-text-white">Por favor ingrese para proceder.</p>
          <div class="box">
            <figure class="avatar">
              <img src="<?php echo base_url(); ?>static/imagenes/udenar.png  " height="128" width="128">
            </figure>
            <form>
              <div class="field">
                <div class="control">
                  <input class="input is-large" type="email" placeholder="Cedula" autofocus="">
                </div>
              </div>

              <div class="field">
                <div class="control">
                  <input class="input is-large" type="password" placeholder="Contraseña">
                </div>
              </div>
              <div class="field">
                <label class="checkbox">
                  <input type="checkbox">
                  Recuerdame
                </label>
              </div>
              <a class="button is-block is-info is-large">Ingresar</a>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</body>
</html>
