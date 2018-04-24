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
    
            $("#formulario").submit(function(evt){
                evt.preventDefault();
                
                $.ajax({
                    url: "modificarPerfilbd.php",
                    type: "post",
                    data: $("#formulario").serialize(),
                    beforeSend: function(){
                        //$("#divcar").html("<img src='ajax-loader.gif'>");
                    },
                    success: function (datos) {
                        $("#formulario").html(datos);
                    }
                });
                
            });
            
        });

    </script>
    
        
        
        
</head>

<body>
		<?php $perfil=$_GET["v"];?>
        <!-- start: Header -->
        <?php include("header.php"); ?>
    
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
                        <h2><i class="halflings-icon white edit"></i><span class="break"></span>Seleccion de test para evaluacion de perfil</h2>
                        <div class="box-icon">
                            <a href="#" class="btn-setting"><i class="halflings-icon white wrench"></i></a>
                            <a href="#" class="btn-minimize"><i class="halflings-icon white chevron-up"></i></a>
                            <a href="#" class="btn-close"><i class="halflings-icon white remove"></i></a>
                        </div>
                    </div>
                    <div class="box-content">
                        <form class="form-horizontal" id="formulario">
                            <fieldset>
                              <div class="control-group">
								<label class="control-label">ID</label>
								<div class="controls">
								  <span class="input-xlarge uneditable-input"><?php echo $perfil; ?></span>
								</div>
							  </div>
							  <div class="control-group">
								<label class="control-label">Cargo</label>
								<div class="controls">
								  <span class="input-xlarge uneditable-input"><?php  
								  		include ("recursos/conecta.php");
                                        $bd = conectar();
                                        $str="";
                                        if (!$bd) return;
                                        $sql="SELECT * FROM perfil INNER JOIN cargo on perfil.cargo = cargo.id WHERE perfil.id = '$perfil' ";
                                        $res = mysqli_query($bd,$sql);
                                        $arr=mysqli_fetch_array($res);
                                        echo $arr[4];
								  		?></span>
								</div>
							  </div>
                              <div class="control-group">
								<label class="control-label" for="selectError1">Multiple Select / Tags</label>
								<div class="controls">
								  <select id="selectError1" multiple data-rel="chosen">
									<?php
										$sql="SELECT * FROM testperfil INNER JOIN test on testperfil.test=test.codigo  WHERE testperfil.perfil = '$perfil'";
										$res = mysqli_query($bd,$sql);
										while($arr=mysqli_fetch_array($res)){
											$str.= "<option value='".$arr[2]."' selected>".$arr[5]."</option>";
										}
										$sql="SELECT * FROM test ";
										$res = mysqli_query($bd,$sql);
										while($arr=mysqli_fetch_array($res)){
											$str.= "<option value='".$arr[0]."'>".$arr[1]."</option>";
										}
										echo $str;

									?>
								  </select>
								</div>
							  </div>
                              
                              <div class="control-group">
                                <label class="control-label" for="focusedInput">Porcentaje minimo</label>
                                <div class="controls">
                                  <input class="input-xlarge " id="focusedInput" type="number" step="0.01" min="0.01" max="1" name="porcentaje" value="" required>
                                </div>
                              </div>
                              
                              <div class="form-actions">
                                <button type="submit" class="btn btn-primary">Guardar</button>
                                <button class="btn">Cancelar</button>
                              </div>
                            </fieldset>
                          </form>
                    
                    </div>
                </div><!--/span-->
            
            </div><!--/row-->
            
            <!--/row-->
    

    </div><!--/.fluid-container-->
    
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
