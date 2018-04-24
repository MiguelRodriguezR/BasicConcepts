<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>RESTAURANTE</title>
        <?php
            include ("./recursos/importarLibrerias.php");
        ?>
    </head>
    <body>
        <div class="container">
            <?php
                include ("./recursos/navegacion.php");
            ?>

            <div id="myCarousel" class="carousel slide myCarousel" data-interval="false" data-ride="carousel">
              <ol class="carousel-indicators">
                <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                <li data-target="#myCarousel" data-slide-to="1"></li>
                <li data-target="#myCarousel" data-slide-to="2"></li>
              </ol> 
              <!-- Carousel items -->
              <div class="carousel-inner">
                <div class="active item">
                  <!--put img inside itens like this-->
                  <!--<img src="" alt="...">-->
                    <img src="images/Ravioli.jpg" alt="...">
                    <div class="container">
                        <div class="carousel-caption">

                            <h3>Reservación de eventos</h3>
                            <p>La solución para su evento empresarial o familiar, reserve con nosotros.</p>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <img src="images/empanadas.jpg" alt="...">
                    <div class="container">
                        <div class="carousel-caption">
                            <h3>Selecta carta de vinos & Licores</h3>
                            <p>La mejor selección de licores, consulte nuestra carta. Vinos 2 X 1</p>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <img src="images/brownie.jpg" alt="...">
                    <div class="container">
                        <div class="carousel-caption">
                            <h3>Domingos Don Pepe</h3>
                            <p>Especiales de domingo Don Pepe, sancocho y ajiaco en familia.</p>
                        </div>
                    </div>
                </div>
            </div>
            <hr class="transition-timer-carousel-progress-bar" />
              <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
              </a>
              <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
              </a>
            </div>

            <div class="jumbotron">
                <h1>Restaurante Gourmet</h1>
                <p>El punto de encuentro con tus amigos y el mejor sitio para pasar en familia </p>
                <hr>
                <a href="empleados/listar.php" class="btn-primary btn-lg">Ver Empleados</a>
                <a href="platos/listar.php" class="btn-primary btn-lg">Ver Platos</a>
            </div>
        </div>
    </body>
</html>
