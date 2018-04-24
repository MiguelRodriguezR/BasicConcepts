<!DOCTYPE html>
<html lang="en">
<head>
    
    <!-- start: Meta -->
    <meta charset="utf-8">
    <title>Bootstrap Metro Dashboard by Dennis Ji for ARM demo</title>
    <meta name="description" content="Bootstrap Metro Dashboard">
    <meta name="author" content="Dennis Ji">
    <meta name="keyword" content="Metro, Metro UI, Dashboard, Bootstrap, Admin, Template, Theme, Responsive, Fluid, Retina">
    <!-- end: Meta -->
    
    <!-- start: Mobile Specific -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- end: Mobile Specific -->
    
    <!-- start: CSS -->
    <link id="bootstrap-style" href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/bootstrap-responsive.min.css" rel="stylesheet">
    <link id="base-style" href="css/style.css" rel="stylesheet">
    <link id="base-style-responsive" href="css/style-responsive.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800&subset=latin,cyrillic-ext,latin-ext' rel='stylesheet' type='text/css'>
    <!-- end: CSS -->
    <?php include("imports.php"); ?>
    

    <!-- The HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <link id="ie-style" href="css/ie.css" rel="stylesheet">
    <![endif]-->
    
    <!--[if IE 9]>
        <link id="ie9style" href="css/ie9.css" rel="stylesheet">
    <![endif]-->
        
    <!-- start: Favicon -->
    <link rel="shortcut icon" href="img/favicon.ico">
    <!-- end: Favicon -->
    <script type="text/javascript">

        $(document).ready(function(){
    
            $(".formulario").submit(function(evt){
                
                evt.preventDefault();
                console.log($("#"+evt.target.id).serialize());
                
                $.ajax({
                    url: "guardarentrevista.php",
                    type: "POST",
                    data: $("#"+evt.target.id).serialize(),
                    beforeSend: function(){
                        //$("#divcar").html("<img src='ajax-loader.gif'>");
                    },
                    success: function (datos) {
                        $("#"+evt.target.id).html(datos);
                    }
                });
                
            });
            
        });

    </script>
    
        
        
        
</head>

<body>
        <!-- start: Header -->
        <?php  include("header.php"); ?>
        <?php $cedula = $_GET["v"]; ?>
    
    <!-- start: Header -->
    
        <div class="container-fluid-full">
        <div class="row-fluid">
                
            <!-- start: Main Menu -->
            <?php include("mainmenu.php"); ?>
            <!-- end: Main Menu -->
            
            <noscript>
                <div class="alert alert-block span10">
                    <h4 class="alert-heading">Warning!</h4>
                    <p>You need to have <a href="http://en.wikipedia.org/wiki/JavaScript" target="_blank">JavaScript</a> enabled to use this site.</p>
                </div>
            </noscript>
            
            <!-- start: Content -->
           <div id="content" class="span10">
            
            
            <ul class="breadcrumb">
                <li>
                    <i class="icon-home"></i>
                    <a href="index.html">Home</a>
                    <i class="icon-angle-right"></i> 
                </li>
                <li>
                    <i class="icon-edit"></i>
                    <a href="#">Forms</a>
                </li>
            </ul>
            
            <!--/row-->
            <div class="row-fluid sortable">        
                <div class="box span12">
                    <div class="box-header" data-original-title>
                        <h2><i class="halflings-icon white user"></i><span class="break"></span>Datos de Aspirante</h2>
                        <div class="box-icon">
                            <a href="#" class="btn-setting"><i class="halflings-icon white wrench"></i></a>
                            <a href="#" class="btn-minimize"><i class="halflings-icon white chevron-up"></i></a>
                            <a href="#" class="btn-close" ><i class="halflings-icon white remove"></i></a>
                        </div>
                    </div>
                    <div class="box-content">
                        <table class="table table-striped table-bordered ">
                          <thead>
                              <tr>
                                  <th>Nombre</th>
                                  <th>Apellido</th>
                                  <th>Cedula</th>
                                  <th>Cargo</th>
                                  <th>Calificacion</th>
                                  <th>Estado</th>
                              </tr>
                          </thead>   
                          <tbody>
                            
                            

                                <?php   
                                $aspirante=null;
                                $perfil=null;
                                include ("recursos/conecta.php");
                                        $bd = conectar();
                                        $str="";
                                        if (!$bd) return;
                                        $sql="SELECT * FROM aspirantes INNER JOIN cargo on aspirantes.cargo = cargo.id WHERE aspirantes.cedula='$cedula' ORDER BY cargo";
                                        $res = mysqli_query($bd,$sql);
                                        $estado='<span class="label label-warning">Pending</span>';
                                        while($arr=mysqli_fetch_array($res)){
                                            if($arr[5]==0){
                                                $estado='<span class="label label-warning">Pendiente</span>';
                                            }
                                            else if($arr[5]==1){
                                                $estado='<span class="label label-success">Aprovado</span>';
                                            }
                                            else{   
                                                $estado='<span class="label label-important">Reprovado</span>';
                                            }
                                            $str.= '    <tr><td>'.$arr[1].'</td>
                                                        <td class="center">'.$arr[2].'</td>
                                                        <td class="center">'.$arr[0].'</td>
                                                        <td class="center">'.$arr[7].'</td>
                                                        <td class="center">'.$arr[3].'</td>
                                                        <td class="center">'.$estado.'</td>
                                                       </tr>'
                                                        ;
                                            $aspirante=$arr[0];
                                            $resp=mysqli_query($bd,"SELECT id FROM perfil WHERE perfil.cargo = '$arr[4]'");
                                            $perfil=mysqli_fetch_array($resp);
                                            $perfil=$perfil[0];
                                        }
                                        echo $str;




                                        
                                ?>
                            
                          </tbody>
                      </table>            
                    </div>
                </div><!--/span-->
            
            </div>

            <?php 

                //echo $perfil[0];
                $str="";
                $sql="";
                $sql="SELECT * FROM testperfil INNER JOIN test on testperfil.test = test.codigo WHERE testperfil.perfil = '$perfil'";
                $res = mysqli_query($bd,$sql);
                
                while($arr=mysqli_fetch_array($res)){
                    $str.= '
                            <div class="row-fluid sortable">
                                <div class="box span12">
                                        <div class="box-header" data-original-title>
                                            <h2><i class="halflings-icon white edit"></i><span class="break"></span>'.$arr[5].'</h2>
                                            <div class="box-icon">
                                                <a href="#" class="btn-setting"><i class="halflings-icon white wrench"></i></a>
                                                <a href="#" class="btn-minimize"><i class="halflings-icon white chevron-up"></i></a>
                                                <a href="#" class="btn-close"><i class="halflings-icon white remove"></i></a>
                                            </div>
                                        </div>
                                        <div class="box-content">
                                        <form class="form-horizontal formulario" id="f'.$arr[2].'">
                                        ';

                                        $test=$arr[2];
                                        $sql2="SELECT * FROM preguntas WHERE preguntas.test='$arr[2]'";
                                        $res2 = mysqli_query($bd,$sql2);
                                        while($arr2=mysqli_fetch_array($res2)){
                                            $str.='
                                                <div class="control-group">
                                                    <label class="control-label" for="focusedInput">'.$arr2[2].'</label>
                                                    <div class="controls">
                                                        <select class="form-control" name="p'.($arr2[1]-(($arr2[0]-1)*10)).'">
                                                            <option value="5">Totalmente de acuerdo</option>
                                                            <option value="4">De acuerdo</option>
                                                            <option value="3">Ni de acuerdo ni en desacuerdo</option>
                                                            <option value="2">En desacuerdo</option>
                                                            <option value="1">Totalmente en desacuerdo</option>
                                                        </select> 
                                                    </div>
                                                  </div>';

                    }



                            $str.= '    <div class="form-actions">
                                        <input type="hidden" name="test" value="'.$test.'">
                                        <input type="hidden" name="aspirante" value="'.$aspirante.'">
                                        <button type="submit" class="btn btn-primary">Guardar</button>
                                        <button class="btn">Cancelar</button>
                                      </div>
                                    </form></div></div><!--/span-->
                                
                                </div> '; 

                }

             echo $str;


            ?>
             
            <!--/row-->
            
            
            <!--/row-->
    

            <!--/.fluid-container-->
    
            <!-- end: Content -->
        </div><!--/#content.span10-->
        </div><!--/fluid-row-->
        
    <div class="modal hide fade" id="myModal">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">×</button>
            <h3>Settings</h3>
        </div>
        <div class="modal-body">
            <p>Here settings can be configured...</p>
        </div>
        <div class="modal-footer">
            <a href="#" class="btn" data-dismiss="modal">Close</a>
            <a href="#" class="btn btn-primary">Save changes</a>
        </div>
    </div>
    
    <div class="common-modal modal fade" id="common-Modal1" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-content">
            <ul class="list-inline item-details">
                <li><a href="http://themifycloud.com">Admin templates</a></li>
                <li><a href="http://themescloud.org">Bootstrap themes</a></li>
            </ul>
        </div>
    </div>
    
    <div class="clearfix"></div>
    
    <footer>

        <p>
            <span style="text-align:left;float:left">&copy; 2016 <a href="http://themifycloud.com/downloads/janux-free-responsive-admin-dashboard-template/" alt="Bootstrap_Metro_Dashboard">sistema de selección de personal</a></span>
            
        </p>

    </footer>
    
    <!-- start: JavaScript-->

        
    <!-- end: JavaScript-->
    
</body>
</html>
