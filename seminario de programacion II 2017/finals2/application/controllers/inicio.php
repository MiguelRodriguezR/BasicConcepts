<?php

  class Inicio extends CI_Controller{
    function index(){
      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="-1";
      $this->load->model("modelo");

      $this->form_validation->set_rules('cedula','Cedula', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('clave','Contraseña', 'required',array('required' => 'debe proveer una %s.'));
      if($datos["tipo"]==""){
        if($this->form_validation->run() == FALSE){
          $this->session->captcha = $this->modelo->pedir_captcha();
          $this->load->view("login",$datos);
        }
        else{
          $e = $this->input->post();
          if($this->session->captcha["val"]==$e["captcha"]){
            $res = $this->modelo->consultar_usuario($this->input->post());
            if($res["cedula"]!=""){
              $this->session->cedula=$res["cedula"];
              $this->session->nombre=$res["nombre"];
              $this->session->apellido=$res["apellido"];
              $this->session->tipo=$res["tipo"];
              $this->session->img=$res["img"];
              redirect(base_url().'inicio','refresh');
            }
            else{
              $datos["error"]="Usuario o contraseña incorrecto";
              $this->load->view("login",$datos);
            }

          }

          else {
            $datos["error"]="captcha incorrecto";
            $this->load->view("login",$datos);
          }
        }
      }
      else{
        $this->load->view("menu");
        $this->load->view("pie");

      }


    }

    function logout(){
      session_destroy();
      redirect(base_url().'inicio','refresh');
    }


    function modificar_usr($ced){
      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");
      $this->form_validation->set_rules('nombre','Nombre', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('apellido','Apellido', 'required',array('required' => 'debe proveer una %s.'));
      if($datos["tipo"]=="administrador"){
        $res = $this->modelo->consultar_usuariopc($ced);
        $this->session->cedulau=$res["cedula"];
        $this->session->nombreu=$res["nombre"];
        $this->session->apellidou=$res["apellido"];
        $this->session->tipou=$res["tipo"];
        $this->session->imgu=$res["img"];
        if($this->form_validation->run() == FALSE){
          $this->load->view("menu");
          $this->load->view("modificar_usr",$datos);
          $this->load->view("pie");
        }
        else{
            $this->modelo->modificar_usuario($this->input->post());
            redirect(base_url().'inicio/usuarios','refresh');
        }
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }


    function eliminar_usr($ced){
      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");

      if($datos["tipo"]=="administrador"){
        $res = $this->modelo->eliminar_usuariopc($ced);
        redirect(base_url().'inicio/usuarios','refresh');
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }

    function crear_evt(){
      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");
      $this->form_validation->set_rules('lugar','Lugar', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('nombre','Nombre', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('valor','Valor', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('fecha_i','Fecha Ingreso', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('fecha_f','Fecha final', 'required',array('required' => 'debe proveer una %s.'));
      if($datos["tipo"]=="administrador"){
        if($this->form_validation->run() == FALSE){
          $this->load->view("menu");
          $this->load->view("crear_evento",$datos);
          $this->load->view("pie");
        }
        else{

            $datos["exito"]=$this->modelo->crear_evento($this->input->post());
            $this->load->view("menu");
            $this->load->view("crear_evento",$datos);
            $this->load->view("pie");
        }
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }


    function agregar_est(){
      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");
      $this->form_validation->set_rules('titulo','Titulo', 'required',array('required' => 'debe proveer una %s.'));
      if($datos["tipo"]=="docente"){
        if($this->form_validation->run() == FALSE){
          $this->load->view("menu");
          $this->load->view("agregar_estudios",$datos);
          $this->load->view("pie");
        }
        else{

            $datos["exito"]=$this->modelo->agregar_estudios($this->input->post());
            $this->load->view("menu");
            $this->load->view("agregar_estudios",$datos);
            $this->load->view("pie");
        }
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }

    function usuarios(){

      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");

      if($datos["tipo"]=="administrador"){
        $res = $this->modelo->consultar_usuarios();
        $datos["respuesta"]=$res;
        $this->load->view("menu");
        $this->load->view("usuarios",$datos);
        $this->load->view("pie");
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }


    function estudios(){

      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");

      if($datos["tipo"]=="docente"){
        $res = $this->modelo->consultar_estudios();
        $datos["respuesta"]=$res;
        $this->load->view("menu");
        $this->load->view("estudios",$datos);
        $this->load->view("pie");
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }

    function productividad(){

      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");

      if($datos["tipo"]=="docente"){
        $res = $this->modelo->consultar_productividad();
        $datos["respuesta"]=$res;
        $this->load->view("menu");
        $this->load->view("productividad",$datos);
        $this->load->view("pie");
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }


    function eventos(){

      $datos["tipo"]=$this->session->tipo;
      $this->load->model("modelo");

      if($datos["tipo"]=="docente"){
        $res = $this->modelo->consultar_fechas();
        $datos["respuesta"]=$res;
        $this->load->view("menu");
        $this->load->view("eventos",$datos);
        $this->load->view("pie");
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }

    function agregar_usr(){
      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");
      $this->form_validation->set_rules('cedula','Cedula', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('nombre','Nombre', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('apellido','Apellido', 'required',array('required' => 'debe proveer una %s.'));
      if($datos["tipo"]=="administrador"){
        if($this->form_validation->run() == FALSE){
          $this->load->view("menu");
          $this->load->view("agregar_usr",$datos);
          $this->load->view("pie");
        }
        else{

            $this->modelo->agregar_usuario($this->input->post());
            $datos["exito"]=" datos agregados con exito";
            $this->load->view("menu");
            $this->load->view("agregar_usr",$datos);
            $this->load->view("pie");
        }
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }

    function perfil(){
      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");
      $this->form_validation->set_rules('nombre','Nombre', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('apellido','Apellido', 'required',array('required' => 'debe proveer una %s.'));
      if($datos["tipo"]!=""){
        if($this->form_validation->run() == FALSE){
          $this->load->view("menu");
          $this->load->view("perfil",$datos);
          $this->load->view("pie");
        }
        else{

            $config['upload_path']     = './static/imagenes/';
            $config['allowed_types']   = 'jpg';
            $config['overwrite']       = TRUE;
            $config['file_name']       = "p".$this->session->cedula;
            $this->load->library('upload', $config);
            if ( ! $this->upload->do_upload('img')){
              $datos["error"]=array('error' => $this->upload->display_errors());
            }else{
              $this->modelo->actualizar_foto();
            }
            $e = $this->input->post();
            $this->modelo->actualizar_nombre($this->input->post());
            $datos["exito"]=" datos actualizados con exito";
            $this->session->nombre=$e["nombre"];
            $this->session->apellido=$e["apellido"];


            $this->load->view("menu");
            $this->load->view("perfil",$datos);
            $this->load->view("pie");
        }
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }


    function agregar_productividad(){
      $datos["tipo"]=$this->session->tipo;
      $datos["error"]="";
      $datos["exito"]="";
      $this->load->model("modelo");
      $this->form_validation->set_rules('titulo','Titulo', 'required',array('required' => 'debe proveer una %s.'));
      $this->form_validation->set_rules('lugar','Lugar', 'required',array('required' => 'debe proveer una %s.'));
      if($datos["tipo"]=="docente"){
        if($this->form_validation->run() == FALSE){
          $this->load->view("menu");
          $this->load->view("agregar_productividad",$datos);
          $this->load->view("pie");
        }
        else{
            $e = $this->input->post();
            $config['upload_path']     = './static/datos/';
            $config['allowed_types']   = 'pdf';
            $config['overwrite']       = TRUE;
            $config['file_name']       = "d".$this->session->cedula."-".$e["fecha_r"];
            $this->load->library('upload', $config);
            if ( ! $this->upload->do_upload('certificado')){
              $datos["error"]=array('error' => $this->upload->display_errors());
            }else{
              $this->modelo->agregar_productividad($this->input->post());
            }
            $this->load->view("menu");
            $this->load->view("agregar_productividad",$datos);
            $this->load->view("pie");
        }
      }
      else{
        session_destroy();
        redirect(base_url().'inicio','refresh');
      }
    }


  }
?>
